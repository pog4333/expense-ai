from ast import Return
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from google import genai
from parsers.pdf_extractor import extract_transactions

transactions_text = extract_transactions("/home/origr/ai_engineer_course/expense-ai/sample_data/ Copy.pdf")
prompt = f"""Extract the transactions from the provided bank statement text.
            Return one object per transaction.
            Each transaction must contain these fields:
            - date
            - description
            - amount
            - ending_day_balance
            Return only a JSON array.
            Do not include markdown or explanatory text. {transactions_text[0]})"""
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input=prompt
)
transaction_json = interaction.output_text
print(transaction_json)