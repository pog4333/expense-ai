from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from google import genai
from app.parsers.pdf_extractor import extract_transactions

transactions_text = extract_transactions("/home/origr/ai_engineer_course/expense-ai/sample_data/ Copy.pdf")
prompt = f"please take this text extracted from bank statement pdf and sort it into a json array of transactions with the following fields: date, description, amount, ending_day_balance. The text is: {transactions_text}"
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input=prompt
)
transaction_json = interaction.output_text
print(transaction_json)