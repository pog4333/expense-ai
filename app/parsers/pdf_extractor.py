from pathlib import Path
from pprint import pprint
import pprint

import pymupdf


def extract_transactions(pdf_path: str | Path) -> tuple[str, int, bool]:
    path = Path(pdf_path)

    if not path.exists():
        return "", 0, False

    try:
        doc = pymupdf.open(path)
        tabs = doc[1].find_tables()  # locate and extract any tables on page

    except (FileNotFoundError, RuntimeError, ValueError):
        return "", 0, False

    try:
        page_count = doc.page_count
        if page_count == 0:
            return "", 0, False

        text = "\n".join(page.get_text() for page in doc)

        start_marker = "Transaction history "
        end_marker = "The Ending Daily Balance does not reflect any pending"

        start_idx = text.find(start_marker)
        if start_idx == -1:
            extracted = ""
        else:
            start_content = start_idx + len(start_marker)
            end_idx = text.find(end_marker, start_content)
            extracted = text[start_content:end_idx] if end_idx != -1 else text[start_content:]

        extracted = extracted.strip()
        return extracted, page_count, bool(extracted)
    finally:
        doc.close()

  

print(extract_transactions("/home/origr/ai_engineer_course/expense-ai/sample_data/ Copy.pdf"))
 # display number of found tables
