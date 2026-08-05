from pathlib import Path

import pymupdf

from app.parsers.pdf_extractor import extract_pdf_text


def test_extract_pdf_text_returns_text_and_page_count(tmp_path: Path) -> None:
    pdf_path = tmp_path / "sample.pdf"
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Hello from PDF")
    page = doc.new_page()
    page.insert_text((72, 72), "Second page")
    doc.save(pdf_path)
    doc.close()

    text, page_count, is_digital = extract_pdf_text(pdf_path)

    assert "Hello from PDF" in text
    assert "Second page" in text
    assert page_count == 2
    assert is_digital is True


def test_extract_first_page_text_handles_missing_file(tmp_path: Path) -> None:
    missing_pdf = tmp_path / "missing.pdf"

    text, page_count, is_digital = extract_first_page_text(missing_pdf)

    assert text == ""
    assert page_count == 0
    assert is_digital is False


def test_extract_first_page_text_rejects_unsupported_file_types(tmp_path: Path) -> None:
    text_file = tmp_path / "sample.txt"
    text_file.write_text("not a pdf")

    text, page_count, is_digital = extract_first_page_text(text_file)

    assert text == ""
    assert page_count == 0
    assert is_digital is False


def test_extract_pdf_text_identifies_scanned_pdf(tmp_path: Path) -> None:
    pdf_path = tmp_path / "scanned.pdf"
    doc = pymupdf.open()
    doc.new_page()
    doc.save(pdf_path)
    doc.close()

    text, page_count, is_digital = extract_pdf_text(pdf_path)

    assert text == ""
    assert page_count == 1
    assert is_digital is False
