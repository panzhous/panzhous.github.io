#!/usr/bin/env python3
"""Update local Google Scholar citation badges for featured publications."""

from __future__ import annotations

import argparse
import html
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from urllib.request import Request, urlopen


SCHOLAR_USER_ID = "0b7ZqlcAAAAJ"
SCHOLAR_PROFILE_URL = (
    "https://scholar.google.com/citations"
    f"?user={SCHOLAR_USER_ID}&hl=en&pagesize=100"
)
DEFAULT_OUTPUT_DIR = (
    Path(__file__).resolve().parents[1] / "assets/img/scholar-citations"
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
        "title_fragment": "weight-decay-integrated nesterov acceleration for faster network training",
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


class ScholarProfileParser(HTMLParser):
    """Extract article IDs, titles, and citation counts from a Scholar profile."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[dict[str, str]] = []
        self._row: dict[str, str] | None = None
        self._field: str | None = None

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        classes = set((attributes.get("class") or "").split())

        if tag == "tr" and "gsc_a_tr" in classes:
            self._row = {"title": "", "href": "", "citations": ""}
            self._field = None
            return

        if tag != "a" or self._row is None:
            return

        if "gsc_a_at" in classes:
            self._field = "title"
            self._row["href"] = attributes.get("href") or ""
        elif "gsc_a_ac" in classes:
            self._field = "citations"

    def handle_data(self, data: str) -> None:
        if self._row is not None and self._field is not None:
            self._row[self._field] += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "a":
            self._field = None
        elif tag == "tr" and self._row is not None:
            self.rows.append(self._row)
            self._row = None
            self._field = None


def fetch(url: str) -> bytes:
    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "Chrome/124.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urlopen(request, timeout=30) as response:
        return response.read()


def normalize_title(value: str) -> str:
    return " ".join(html.unescape(value).casefold().split())


def parse_profile(profile_html: str) -> dict[str, dict[str, str | int]]:
    parser = ScholarProfileParser()
    parser.feed(profile_html)
    records: dict[str, dict[str, str | int]] = {}

    for row in parser.rows:
        query = parse_qs(urlsplit(html.unescape(row["href"])).query)
        citation_ids = query.get("citation_for_view", [])
        if not citation_ids:
            continue

        digits = re.sub(r"[^0-9]", "", row["citations"])
        records[citation_ids[0]] = {
            "title": row["title"].strip(),
            "citations": int(digits) if digits else 0,
        }

    if not records:
        raise RuntimeError("No publication records found in the Google Scholar response")
    return records


def download_badge(citations: int) -> bytes:
    badge_url = (
        "https://img.shields.io/badge/"
        f"Citations-{citations}-blue?style=social&logo=googlescholar"
    )
    badge = fetch(badge_url)
    if not badge.lstrip().startswith(b"<svg"):
        raise RuntimeError("Shields.io did not return an SVG badge")
    return badge.rstrip() + b"\n"


def update_badges(profile_html: str, output_dir: Path) -> None:
    records = parse_profile(profile_html)
    generated: dict[str, tuple[bytes, int, str]] = {}

    for slug, paper in FEATURED_PAPERS.items():
        citation_id = paper["citation_id"]
        record = records.get(citation_id)
        if record is None:
            raise RuntimeError(f"Featured publication not found: {citation_id}")

        title = str(record["title"])
        if paper["title_fragment"] not in normalize_title(title):
            raise RuntimeError(
                f"Google Scholar article ID no longer matches the expected paper: {title}"
            )

        citations = int(record["citations"])
        generated[slug] = (download_badge(citations), citations, title)

    output_dir.mkdir(parents=True, exist_ok=True)
    for slug, (badge, citations, title) in generated.items():
        destination = output_dir / f"{slug}.svg"
        if not destination.exists() or destination.read_bytes() != badge:
            destination.write_bytes(badge)
        print(f"{slug}: {citations} citations — {title}")


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--profile-html",
        type=Path,
        help="Read a saved Google Scholar profile instead of downloading it",
    )
    argument_parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for generated SVG badges",
    )
    arguments = argument_parser.parse_args()

    if arguments.profile_html:
        profile_html = arguments.profile_html.read_text(
            encoding="utf-8", errors="replace"
        )
    else:
        profile_html = fetch(SCHOLAR_PROFILE_URL).decode("utf-8", errors="replace")

    update_badges(profile_html, arguments.output_dir)


if __name__ == "__main__":
    main()
