from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
SCRIPT_PATH = SCRIPTS_DIR / "update_google_scholar_badges.py"
FIXTURE_PATH = SCRIPTS_DIR / "fixtures/serpapi_google_scholar_author.json"

SPEC = importlib.util.spec_from_file_location("citation_badges", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to import citation badge updater")
CITATION_BADGES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CITATION_BADGES)


class CitationBadgeUpdaterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.records = CITATION_BADGES.parse_serpapi_profile(self.payload)

    def test_fixture_contains_every_featured_publication(self) -> None:
        expected_ids = {
            paper["citation_id"] for paper in CITATION_BADGES.FEATURED_PAPERS.values()
        }
        self.assertEqual(expected_ids, set(self.records))

    def test_generates_all_badges_without_network_access(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "badges"
            CITATION_BADGES.update_badges(self.records, output_dir)

            badges = sorted(output_dir.glob("*.svg"))
            self.assertEqual(len(CITATION_BADGES.FEATURED_PAPERS), len(badges))
            metaformer = (output_dir / "metaformer-original.svg").read_text(
                encoding="utf-8"
            )
            self.assertIn('aria-label="Citations: 2017"', metaformer)
            self.assertIn("data:image/svg+xml;base64,", metaformer)

    def test_missing_publication_does_not_overwrite_existing_badges(self) -> None:
        missing_records = dict(self.records)
        missing_records.pop("0b7ZqlcAAAAJ:mB3voiENLucC")

        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "badges"
            output_dir.mkdir()
            existing_badge = output_dir / "metaformer-original.svg"
            existing_badge.write_bytes(b"existing badge")

            with self.assertRaisesRegex(RuntimeError, "not found"):
                CITATION_BADGES.update_badges(missing_records, output_dir)

            self.assertEqual(b"existing badge", existing_badge.read_bytes())

    def test_large_decrease_requires_explicit_override(self) -> None:
        changed_records = {
            citation_id: dict(record) for citation_id, record in self.records.items()
        }
        changed_records["0b7ZqlcAAAAJ:mB3voiENLucC"]["citations"] = 10

        with tempfile.TemporaryDirectory() as temporary_directory:
            output_dir = Path(temporary_directory) / "badges"
            output_dir.mkdir()
            existing_badge = output_dir / "metaformer-original.svg"
            existing_badge.write_bytes(CITATION_BADGES.render_badge(2017))

            with self.assertRaisesRegex(RuntimeError, "dropped unexpectedly"):
                CITATION_BADGES.update_badges(changed_records, output_dir)

            self.assertEqual(
                CITATION_BADGES.render_badge(2017), existing_badge.read_bytes()
            )

    def test_api_error_is_reported(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "quota exceeded"):
            CITATION_BADGES.parse_serpapi_profile({"error": "quota exceeded"})

    def test_fetches_a_second_page_when_a_featured_paper_is_missing(self) -> None:
        articles = list(self.payload["articles"])
        final_article = articles.pop()
        first_page = {
            "articles": articles
            + [
                {
                    "title": f"Unrelated paper {index}",
                    "citation_id": f"other:{index}",
                    "cited_by": {"value": index},
                }
                for index in range(92)
            ]
        }
        pages = [first_page, {"articles": [final_article]}]
        requested_urls: list[str] = []
        original_fetch_json = CITATION_BADGES.fetch_json

        def fake_fetch_json(url: str) -> dict[str, object]:
            requested_urls.append(url)
            return pages.pop(0)

        CITATION_BADGES.fetch_json = fake_fetch_json
        try:
            records = CITATION_BADGES.fetch_serpapi_profile("test-key")
        finally:
            CITATION_BADGES.fetch_json = original_fetch_json

        self.assertEqual(set(self.records), set(records).intersection(self.records))
        self.assertEqual(2, len(requested_urls))
        self.assertIn("start=100", requested_urls[1])


if __name__ == "__main__":
    unittest.main()
