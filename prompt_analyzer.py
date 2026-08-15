def analyze_prompt(prompt: str) -> dict:
    prompt = prompt.strip()

    if not prompt:
        return {
            "score": 0,
            "clarity": 0,
            "context": 0,
            "specificity": 0,
            "constraints": 0,
            "output_format": 0,
            "suggestions": ["Enter a prompt to analyze."]
        }

    words = prompt.split()
    word_count = len(words)

    clarity = min(100, 40 + word_count * 2)

    context_keywords = [
        "context", "background", "for", "because",
        "using", "about", "based on"
    ]
    context = min(
        100,
        30 + sum(15 for word in context_keywords if word in prompt.lower())
    )

    specificity_keywords = [
        "explain", "compare", "analyze", "generate",
        "create", "describe", "provide"
    ]
    specificity = min(
        100,
        30 + sum(10 for word in specificity_keywords if word in prompt.lower())
    )

    constraint_keywords = [
        "limit", "words", "format", "must",
        "should", "avoid", "include"
    ]
    constraints = min(
        100,
        20 + sum(15 for word in constraint_keywords if word in prompt.lower())
    )

    output_keywords = [
        "table", "list", "steps", "json",
        "markdown", "bullet", "code"
    ]
    output_format = min(
        100,
        20 + sum(15 for word in output_keywords if word in prompt.lower())
    )

    score = round(
        (
            clarity
            + context
            + specificity
            + constraints
            + output_format
        ) / 5
    )

    suggestions = []

    if clarity < 60:
        suggestions.append("Make the task more explicit.")

    if context < 60:
        suggestions.append("Add relevant background or context.")

    if specificity < 60:
        suggestions.append("Specify exactly what you want the AI to do.")

    if constraints < 60:
        suggestions.append("Add constraints such as length, style, or requirements.")

    if output_format < 60:
        suggestions.append("Specify the desired output format.")

    return {
        "score": score,
        "clarity": clarity,
        "context": context,
        "specificity": specificity,
        "constraints": constraints,
        "output_format": output_format,
        "suggestions": suggestions
    }
