import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash"


def detect_output_format(prompt: str) -> str:

    instruction = f"""
Analyze this user prompt:

{prompt}

Determine the most appropriate output format.

Choose ONE:

- Explanation
- Step-by-step guide
- Bullet list
- Table
- Code
- JSON
- Essay
- Summary
- Comparison
- Other

Return only the format name.
"""

    interaction = client.interactions.create(
        model=MODEL,
        input=instruction
    )

    return interaction.output_text.strip()
