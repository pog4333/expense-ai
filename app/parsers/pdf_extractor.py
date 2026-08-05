from pathlib import Path

import pymupdf


def extract_pdf_text(pdf_path: str | Path) -> tuple[str, int, bool]:
    path = Path(pdf_path)

    if not path.exists():
        return "", 0, False

    try:
        doc = pymupdf.open(path)
    except (FileNotFoundError, RuntimeError, ValueError):
        return "", 0, False

    try:
        if doc.type_name.lower() != "pdf":
            return "", 0, False

        page_count = doc.page_count
        if page_count == 0:
            return "", 0, False

        text = "\n".join(page.get_text() for page in doc)
        return text, page_count, bool(text.strip())
    finally:
        doc.close()
