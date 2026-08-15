import json
import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash"


def evaluate_prompt(prompt: str) -> dict:

    evaluation_prompt = f"""
You are an expert Prompt Engineering evaluator.

Evaluate the following prompt:

{prompt}

Score these categories from 0 to 100:

- clarity
- context
- specificity
- constraints
- output_format

Also provide:

- overall_score
- strengths
- weaknesses
- suggestions

Return ONLY valid JSON.

Use exactly this structure:

{{
    "overall_score": 0,
    "clarity": 0,
    "context": 0,
    "specificity": 0,
    "constraints": 0,
    "output_format": 0,
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}
"""

    interaction = client.interactions.create(
        model=MODEL,
        input=evaluation_prompt
    )

    response_text = interaction.output_text.strip()

    try:
        return json.loads(response_text)

    except json.JSONDecodeError:

        return {
            "overall_score": 0,
            "clarity": 0,
            "context": 0,
            "specificity": 0,
            "constraints": 0,
            "output_format": 0,
            "strengths": [],
            "weaknesses": [
                "AI returned an invalid evaluation format."
            ],
            "suggestions": [
                "Try analyzing the prompt again."
            ]
        }
