import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.parsers.pdf_extractor import extract_transactions


def _write_pdf(pdf_path: Path, text: str) -> None:
    doc = pymupdf.open()
    if text:
        page = doc.new_page()
        page.insert_text((72, 72), text)
    doc.save(str(pdf_path))
    doc.close()


def test_extract_transactions_success(tmp_path):
    pdf_path = tmp_path / "success.pdf"
    _write_pdf(
        pdf_path,
        "Header text\nTransaction history \n2026-01-01 Purchase -100.00\n"
        "The Ending Daily Balance does not reflect any pending\nFooter",
    )

    extracted, page_count, ok = extract_transactions(pdf_path)

    assert page_count == 1
    assert ok is True
    assert extracted == "2026-01-01 Purchase -100.00"


def test_extract_transactions_missing_start_marker(tmp_path):
    pdf_path = tmp_path / "missing_start.pdf"
    _write_pdf(
        pdf_path,
        "Header text without the marker\nThe Ending Daily Balance does not reflect any pending",
    )

    extracted, page_count, ok = extract_transactions(pdf_path)

    assert page_count == 1
    assert extracted == ""
    assert ok is False


def test_extract_transactions_missing_end_marker(tmp_path):
    pdf_path = tmp_path / "missing_end.pdf"
    _write_pdf(
        pdf_path,
        "Transaction history \n2026-01-02 Deposit 500.00\nNo closing marker present",
    )

    extracted, page_count, ok = extract_transactions(pdf_path)

    assert page_count == 1
    assert ok is True
    assert extracted == "2026-01-02 Deposit 500.00\nNo closing marker present"


def test_extract_transactions_nonexistent_file(tmp_path):
    pdf_path = tmp_path / "does_not_exist.pdf"

    extracted, page_count, ok = extract_transactions(pdf_path)

    assert extracted == ""
    assert page_count == 0
    assert ok is False


def test_extract_transactions_empty_pdf(tmp_path):
    pdf_path = tmp_path / "empty.pdf"
    doc = pymupdf.open()
    doc.save(str(pdf_path))
    doc.close()

    extracted, page_count, ok = extract_transactions(pdf_path)

    assert extracted == ""
    assert page_count == 0
    assert ok is False