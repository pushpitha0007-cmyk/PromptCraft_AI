import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


MODEL = "gemini-3.5-flash"


def optimize_with_ai(prompt: str) -> str:
    interaction = client.interactions.create(
        model=MODEL,
        input=prompt
    )

    return interaction.output_text
