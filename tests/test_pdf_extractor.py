from pathlib import Path

import pymupdf

from app.parsers.pdf_extractor import extract_first_page_text


def test_extract_first_page_text_returns_text_and_page_count(tmp_path: Path) -> None:
    pdf_path = tmp_path / "sample.pdf"
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Hello from PDF")
    doc.save(pdf_path)
    doc.close()

    text, page_count = extract_first_page_text(pdf_path)

    assert text == "Hello from PDF"
    assert page_count == 1


def test_extract_first_page_text_handles_missing_file(tmp_path: Path) -> None:
    missing_pdf = tmp_path / "missing.pdf"

    text, page_count = extract_first_page_text(missing_pdf)

    assert text == ""
    assert page_count == 0
