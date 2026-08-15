def calculate_final_risk(
    rule_score: int,
    ai_score: int
) -> dict:

    final_score = round(
        (rule_score * 0.4) +
        (ai_score * 0.6)
    )

    if final_score >= 75:
        level = "High"

    elif final_score >= 50:
        level = "Medium"

    elif final_score >= 25:
        level = "Low"

    else:
        level = "Safe"

    return {
        "score": final_score,
        "level": level
    }
