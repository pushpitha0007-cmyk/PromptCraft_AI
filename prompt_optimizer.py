def build_optimization_prompt(user_prompt: str, mode: str) -> str:

    strategies = STRATEGIES.get(
        mode,
        STRATEGIES["General"]
    )

    strategy_text = "\n".join(
        f"- {strategy}"
        for strategy in strategies
    )

    return f"""
You are an expert Prompt Engineer and Generative AI specialist.

Your job is to analyze and improve the user's prompt.

USER PROMPT:
{user_prompt}

OPTIMIZATION MODE:
{mode}

Analyze the prompt using these dimensions:

1. Clarity
2. Context
3. Specificity
4. Constraints
5. Expected Output Format
6. Role / Persona
7. Task Objective

Then create an improved version of the prompt.

IMPORTANT RULES:

- Preserve the original intent.
- Do not invent requirements that change the user's goal.
- Add useful context only when necessary.
- Make vague instructions specific.
- Add constraints when they improve the result.
- Define the expected output format.
- Use an appropriate AI role when useful.
- Make the prompt easy for an LLM to understand.

Return your answer using EXACTLY this structure:

ANALYSIS:
<short explanation>

STRENGTHS:
- <strength>
- <strength>

WEAKNESSES:
- <weakness>
- <weakness>

OPTIMIZED PROMPT:
<optimized prompt>

EXPECTED OUTPUT:
<description of what the AI should return>

OPTIMIZATION STRATEGIES:
{strategy_text}

"""
STRATEGIES = {
    "General": [
        "Improve clarity",
        "Add useful context",
        "Specify the expected output"
    ],

    "Academic": [
        "Define the learning objective",
        "Use educational explanations",
        "Include examples"
    ],

    "Coding": [
        "Define programming language",
        "Specify requirements",
        "Request clean and maintainable code"
    ],

    "AI / ML": [
        "Define the AI/ML task",
        "Specify technical requirements",
        "Request structured explanations"
    ],

    "Cybersecurity": [
        "Define the security context",
        "Specify the security objective",
        "Request safe and ethical guidance"
    ],

    "Research": [
        "Define the research question",
        "Specify evidence requirements",
        "Request structured analysis"
    ],

    "Professional": [
        "Define the professional context",
        "Use appropriate tone",
        "Specify the desired deliverable"
    ],

    "Creative": [
        "Define the creative direction",
        "Specify style",
        "Provide constraints"
    ]
}
