import os
from pathlib import Path

import pymupdf
import requests
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
dotenv_path = BASE_DIR / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)
else:
    load_dotenv(BASE_DIR / ".env.example")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def extract_transactions(pdf_path: str | Path) -> tuple[str, int, bool]:
    path = Path(pdf_path)

    if not path.exists():
        return "", 0, False

    try:
        doc = pymupdf.open(path)
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


def ask_gemini_for_sorted_json(transactions_text: str) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not set in .env or .env.example")

    prompt = (
        "Parse the extracted transaction text below and return only valid JSON. "
        "Sort the transactions chronologically and return an array of objects. "
        "Each object should include date, description, amount, and any balance information "
        "that can be parsed reliably.\n\n"
        f"{transactions_text}"
    )

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
        },
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    sample_file = BASE_DIR / "sample_data" / " Copy.pdf"
    extracted, page_count, ok = extract_transactions(sample_file)
    if not ok:
        print("No transactions found.")
    else:
        sorted_json = ask_gemini_for_sorted_json(extracted)
        output_file = BASE_DIR / "sorted_transactions.json"
        output_file.write_text(sorted_json, encoding="utf-8")
        print(f"Saved sorted JSON to {output_file}")
