from pathlib import Path

import pymupdf


def extract_first_page_text(pdf_path: str | Path) -> tuple[str, int]:
    path = Path(pdf_path)

    if not path.exists():
        return "", 0

    try:
        doc = pymupdf.open(path)
    except (FileNotFoundError, RuntimeError, ValueError):
        return "", 0

    try:
        page_count = doc.page_count
        if page_count == 0:
            return "", 0

        return doc[0].get_text(), page_count
    finally:
        doc.close()
