#!/usr/bin/env python3
"""Update local Google Scholar citation badges through the SerpApi API."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import socket
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


SCHOLAR_USER_ID = "0b7ZqlcAAAAJ"
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"
SERPAPI_PAGE_SIZE = 100
SERPAPI_MAX_PAGES = 10
DEFAULT_OUTPUT_DIR = (
    Path(__file__).resolve().parents[1] / "assets/img/scholar-citations"
)
RETRYABLE_HTTP_STATUS_CODES = {429, 500, 502, 503, 504}
MAX_CITATION_DROP_RATIO = 0.20
EXISTING_COUNT_PATTERN = re.compile(rb'aria-label="Citations: ([0-9]+)"')
GOOGLE_SCHOLAR_ICON = (
    "PHN2ZyBmaWxsPSIjNDI4NUY0IiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIg"
    "eG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+R29vZ2xlIFNj"
    "aG9sYXI8L3RpdGxlPjxwYXRoIGQ9Ik01LjI0MiAxMy43NjlMMCA5LjUgMTIgMGwxMiA5"
    "LjUtNS4yNDIgNC4yNjlDMTcuNTQ4IDExLjI0OSAxNC45NzggOS41IDEyIDkuNWMtMi45"
    "NzcgMC01LjU0OCAxLjc0OC02Ljc1OCA0LjI2OXpNMTIgMTBhNyA3IDAgMSAwIDAgMTQg"
    "NyA3IDAgMCAwIDAtMTR6Ii8+PC9zdmc+"
)

# Use stable article IDs from the public profile instead of matching by title alone.
FEATURED_PAPERS = {
    "metaformer-original": {
        "citation_id": f"{SCHOLAR_USER_ID}:mB3voiENLucC",
        "title_fragment": "metaformer is actually what you need for vision",
    },
    "pcl": {
        "citation_id": f"{SCHOLAR_USER_ID}:Zph67rFs4hoC",
        "title_fragment": "prototypical contrastive learning",
    },
    "mdt": {
        "citation_id": f"{SCHOLAR_USER_ID}:lSLTfruPkqcC",
        "title_fragment": "masked diffusion transformer is a strong image synthesizer",
    },
    "consistent3d": {
        "citation_id": f"{SCHOLAR_USER_ID}:fPk4N6BV_jEC",
        "title_fragment": "consistent3d: towards consistent high-fidelity",
    },
    "adan": {
        "citation_id": f"{SCHOLAR_USER_ID}:TFP_iSt0sucC",
        "title_fragment": "adan: adaptive nesterov momentum",
    },
    "win": {
        "citation_id": f"{SCHOLAR_USER_ID}:bFI3QPDXJZMC",
        "title_fragment": (
            "weight-decay-integrated nesterov acceleration for faster network "
            "training"
        ),
    },
    "loco": {
        "citation_id": f"{SCHOLAR_USER_ID}:Mojj43d5GZwC",
        "title_fragment": "loco: low-bit communication adaptor",
    },
    "adamw": {
        "citation_id": f"{SCHOLAR_USER_ID}:ns9cj8rnVeAC",
        "title_fragment": "towards understanding convergence and generalization of adamw",
    },
    "sgd-generalization": {
        "citation_id": f"{SCHOLAR_USER_ID}:4TOpqqG69KYC",
        "title_fragment": "why sgd generalizes better than adam",
    },
}


def fetch(url: str, *, retries: int = 3) -> bytes:
    """Fetch a URL with bounded retries for transient network failures."""
    request = Request(
        url,
        headers={
            "User-Agent": "panzhous.github.io-citation-updater/1.0",
            "Accept": "application/json",
        },
    )

    for attempt in range(retries):
        try:
            with urlopen(request, timeout=30) as response:
                return response.read()
        except HTTPError as error:
            should_retry = error.code in RETRYABLE_HTTP_STATUS_CODES
            if not should_retry or attempt == retries - 1:
                raise
        except (URLError, TimeoutError, socket.timeout):
            if attempt == retries - 1:
                raise

        time.sleep(2**attempt)

    raise RuntimeError("Citation request exhausted its retry budget")


def fetch_json(url: str) -> dict[str, object]:
    """Fetch and validate a JSON object without exposing the request URL."""
    try:
        payload = json.loads(fetch(url).decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError("SerpApi did not return valid JSON") from error

    if not isinstance(payload, dict):
        raise RuntimeError("SerpApi returned a non-object JSON response")
    return payload


def normalize_title(value: str) -> str:
    return " ".join(html.unescape(value).casefold().split())


def parse_serpapi_page(
    payload: dict[str, object],
) -> tuple[dict[str, dict[str, str | int]], int]:
    """Extract article IDs, titles, and citation counts from one API page."""
    api_error = payload.get("error")
    if api_error:
        raise RuntimeError(f"SerpApi reported an error: {api_error}")

    articles = payload.get("articles")
    if not isinstance(articles, list):
        raise RuntimeError("SerpApi response did not include an articles list")

    records: dict[str, dict[str, str | int]] = {}
    for article in articles:
        if not isinstance(article, dict):
            continue

        citation_id = article.get("citation_id")
        title = article.get("title")
        cited_by = article.get("cited_by")
        if not isinstance(citation_id, str) or not isinstance(title, str):
            continue

        citation_count: object = 0
        if isinstance(cited_by, dict):
            citation_count = cited_by.get("value", 0)

        if isinstance(citation_count, bool):
            raise RuntimeError(f"Invalid citation count for {citation_id}")
        try:
            parsed_count = int(citation_count)
        except (TypeError, ValueError) as error:
            raise RuntimeError(
                f"Invalid citation count for {citation_id}: {citation_count}"
            ) from error
        if parsed_count < 0:
            raise RuntimeError(f"Negative citation count for {citation_id}")

        records[citation_id] = {
            "title": title.strip(),
            "citations": parsed_count,
        }

    return records, len(articles)


def parse_serpapi_profile(
    payload: dict[str, object],
) -> dict[str, dict[str, str | int]]:
    """Parse a saved single-page SerpApi profile response."""
    records, _ = parse_serpapi_page(payload)
    return records


def fetch_serpapi_profile(api_key: str) -> dict[str, dict[str, str | int]]:
    """Fetch profile pages until every featured publication has been found."""
    expected_ids = {str(paper["citation_id"]) for paper in FEATURED_PAPERS.values()}
    records: dict[str, dict[str, str | int]] = {}

    for page_number in range(SERPAPI_MAX_PAGES):
        parameters = urlencode(
            {
                "engine": "google_scholar_author",
                "author_id": SCHOLAR_USER_ID,
                "hl": "en",
                "num": SERPAPI_PAGE_SIZE,
                "start": page_number * SERPAPI_PAGE_SIZE,
                "api_key": api_key,
            }
        )
        page_records, article_count = parse_serpapi_page(
            fetch_json(f"{SERPAPI_ENDPOINT}?{parameters}")
        )
        records.update(page_records)

        if expected_ids.issubset(records):
            return records
        if article_count < SERPAPI_PAGE_SIZE:
            break

    missing_ids = sorted(expected_ids.difference(records))
    raise RuntimeError(
        "Featured publications were not found in the SerpApi response: "
        + ", ".join(missing_ids)
    )


def render_badge(citations: int) -> bytes:
    """Render the existing social-style badge without another network request."""
    citation_text = str(citations)
    value_width = 9 + 6 * len(citation_text)
    total_width = 81 + value_width
    value_center = int((80 + value_width / 2) * 10)
    value_text_width = (value_width - 8) * 10
    label = f"Citations: {citation_text}"

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" '
        f'height="20" role="img" aria-label="{label}"><title>{label}</title>'
        "<style>a:hover #llink{fill:url(#b);stroke:#ccc}"
        "a:hover #rlink{fill:#4183c4}</style>"
        '<linearGradient id="a" x2="0" y2="100%"><stop offset="0" '
        'stop-color="#fcfcfc" stop-opacity="0"/><stop offset="1" '
        'stop-opacity=".1"/></linearGradient><linearGradient id="b" x2="0" '
        'y2="100%"><stop offset="0" stop-color="#ccc" stop-opacity=".1"/>'
        '<stop offset="1" stop-opacity=".1"/></linearGradient>'
        '<g stroke="#d5d5d5"><rect stroke="none" fill="#fcfcfc" x=".5" '
        'y=".5" width="74" height="19" rx="2"/>'
        f'<rect x="80.5" y=".5" width="{value_width}" height="19" rx="2" '
        'fill="#fafafa"/><rect x="80" y="7.5" width=".5" height="5" '
        'stroke="#fafafa"/><path d="M80.5 6.5 l-3 3v1 l3 3" '
        'fill="#fafafa"/></g>'
        f'<image x="5" y="3" width="14" height="14" '
        f'href="data:image/svg+xml;base64,{GOOGLE_SCHOLAR_ICON}"/>'
        '<g aria-hidden="true" fill="#333" text-anchor="middle" '
        'font-family="Helvetica Neue,Helvetica,Arial,sans-serif" '
        'text-rendering="geometricPrecision" font-weight="700" font-size="110px" '
        'line-height="14px"><rect id="llink" stroke="#d5d5d5" fill="url(#a)" '
        'x=".5" y=".5" width="74" height="19" rx="2"/>'
        '<text aria-hidden="true" x="455" y="150" fill="#fff" '
        'transform="scale(.1)" textLength="470">Citations</text>'
        '<text x="455" y="140" transform="scale(.1)" '
        'textLength="470">Citations</text>'
        f'<text aria-hidden="true" x="{value_center}" y="150" fill="#fff" '
        f'transform="scale(.1)" textLength="{value_text_width}">{citation_text}</text>'
        f'<text id="rlink" x="{value_center}" y="140" transform="scale(.1)" '
        f'textLength="{value_text_width}">{citation_text}</text></g></svg>\n'
    )
    return svg.encode("utf-8")


def read_existing_count(path: Path) -> int | None:
    if not path.exists():
        return None
    match = EXISTING_COUNT_PATTERN.search(path.read_bytes())
    return int(match.group(1)) if match else None


def validate_records(records: dict[str, dict[str, str | int]]) -> None:
    """Ensure every configured ID still resolves to the intended paper."""
    for paper in FEATURED_PAPERS.values():
        citation_id = str(paper["citation_id"])
        record = records.get(citation_id)
        if record is None:
            raise RuntimeError(f"Featured publication not found: {citation_id}")

        title = str(record["title"])
        if str(paper["title_fragment"]) not in normalize_title(title):
            raise RuntimeError(
                f"Google Scholar article ID no longer matches the expected paper: {title}"
            )


def update_badges(
    records: dict[str, dict[str, str | int]],
    output_dir: Path,
    *,
    allow_large_decrease: bool = False,
) -> None:
    """Validate all records, then update every changed badge."""
    validate_records(records)
    generated: dict[str, tuple[bytes, int, str]] = {}

    for slug, paper in FEATURED_PAPERS.items():
        citation_id = str(paper["citation_id"])
        record = records[citation_id]
        citations = int(record["citations"])
        title = str(record["title"])
        destination = output_dir / f"{slug}.svg"
        existing_count = read_existing_count(destination)

        if (
            not allow_large_decrease
            and existing_count
            and citations < existing_count * (1 - MAX_CITATION_DROP_RATIO)
        ):
            raise RuntimeError(
                f"Citation count for {slug} dropped unexpectedly from "
                f"{existing_count} to {citations}; rerun with "
                "--allow-large-decrease after verifying the source"
            )

        generated[slug] = (render_badge(citations), citations, title)

    output_dir.mkdir(parents=True, exist_ok=True)
    for slug, (badge, citations, title) in generated.items():
        destination = output_dir / f"{slug}.svg"
        if not destination.exists() or destination.read_bytes() != badge:
            temporary_destination = destination.with_suffix(".svg.tmp")
            temporary_destination.write_bytes(badge)
            temporary_destination.replace(destination)
        print(f"{slug}: {citations} citations — {title}")


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--input-json",
        type=Path,
        help="Read a saved SerpApi author response instead of calling the API",
    )
    argument_parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for generated SVG badges",
    )
    argument_parser.add_argument(
        "--allow-large-decrease",
        action="store_true",
        help="Accept a verified citation decrease greater than 20 percent",
    )
    arguments = argument_parser.parse_args()

    if arguments.input_json:
        try:
            payload = json.loads(arguments.input_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise RuntimeError("Input fixture is not valid JSON") from error
        if not isinstance(payload, dict):
            raise RuntimeError("Input fixture must contain a JSON object")
        records = parse_serpapi_profile(payload)
    else:
        api_key = os.environ.get("SERPAPI_KEY", "").strip()
        if not api_key:
            raise RuntimeError(
                "SERPAPI_KEY is required when --input-json is not provided"
            )
        records = fetch_serpapi_profile(api_key)

    update_badges(
        records,
        arguments.output_dir,
        allow_large_decrease=arguments.allow_large_decrease,
    )


if __name__ == "__main__":
    main()
