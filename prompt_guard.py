import re


PATTERNS = {
    "instruction_override": [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"ignore\s+(all\s+)?prior\s+instructions",
        r"disregard\s+(all\s+)?previous\s+instructions",
        r"forget\s+(all\s+)?previous\s+instructions",
    ],

    "system_prompt_extraction": [
        r"reveal\s+(your\s+)?system\s+prompt",
        r"show\s+(me\s+)?your\s+system\s+prompt",
        r"print\s+(your\s+)?system\s+instructions",
        r"what\s+are\s+your\s+hidden\s+instructions",
        r"tell\s+me\s+your\s+hidden\s+prompt",
    ],

    "secret_extraction": [
        r"reveal\s+(the\s+)?api\s*key",
        r"show\s+(me\s+)?the\s+api\s*key",
        r"give\s+me\s+(your\s+)?password",
        r"reveal\s+(your\s+)?credentials",
        r"show\s+me\s+your\s+secrets",
    ],

    "restriction_bypass": [
        r"bypass\s+(your\s+)?restrictions",
        r"bypass\s+(your\s+)?safety",
        r"disable\s+(your\s+)?safety",
        r"ignore\s+safety",
        r"remove\s+your\s+restrictions",
    ],

    "role_manipulation": [
        r"you\s+are\s+now\s+dan",
        r"you\s+are\s+now\s+an?\s+unrestricted",
        r"pretend\s+you\s+have\s+no\s+rules",
        r"act\s+as\s+an?\s+unrestricted\s+ai",
    ],
}


def scan_prompt(prompt: str) -> dict:
    """
    Scan a prompt for common prompt-injection indicators.
    """

    prompt_lower = prompt.lower()

    findings = []
    categories = set()

    for category, patterns in PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, prompt_lower):

                findings.append({
                    "category": category,
                    "pattern": pattern,
                    "severity": "high"
                })

                categories.add(category)

                break

    if not findings:

        return {
            "safe": True,
            "risk_score": 0,
            "risk_level": "Low",
            "findings": [],
            "recommendation": "No obvious prompt injection indicators detected."
        }

    risk_score = min(
        100,
        len(findings) * 25
    )

    if risk_score >= 75:
        risk_level = "High"
    elif risk_score >= 50:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "safe": False,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "findings": findings,
        "recommendation": (
            "Review the prompt before sending it to the model. "
            "Do not expose system instructions, credentials, or secrets."
        )
    }import re


PATTERNS = {
    "instruction_override": [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"ignore\s+(all\s+)?prior\s+instructions",
        r"disregard\s+(all\s+)?previous\s+instructions",
        r"forget\s+(all\s+)?previous\s+instructions",
    ],

    "system_prompt_extraction": [
        r"reveal\s+(your\s+)?system\s+prompt",
        r"show\s+(me\s+)?your\s+system\s+prompt",
        r"print\s+(your\s+)?system\s+instructions",
        r"what\s+are\s+your\s+hidden\s+instructions",
        r"tell\s+me\s+your\s+hidden\s+prompt",
    ],

    "secret_extraction": [
        r"reveal\s+(the\s+)?api\s*key",
        r"show\s+(me\s+)?the\s+api\s*key",
        r"give\s+me\s+(your\s+)?password",
        r"reveal\s+(your\s+)?credentials",
        r"show\s+me\s+your\s+secrets",
    ],

    "restriction_bypass": [
        r"bypass\s+(your\s+)?restrictions",
        r"bypass\s+(your\s+)?safety",
        r"disable\s+(your\s+)?safety",
        r"ignore\s+safety",
        r"remove\s+your\s+restrictions",
    ],

    "role_manipulation": [
        r"you\s+are\s+now\s+dan",
        r"you\s+are\s+now\s+an?\s+unrestricted",
        r"pretend\s+you\s+have\s+no\s+rules",
        r"act\s+as\s+an?\s+unrestricted\s+ai",
    ],
}


def scan_prompt(prompt: str) -> dict:
    """
    Scan a prompt for common prompt-injection indicators.
    """

    prompt_lower = prompt.lower()

    findings = []
    categories = set()

    for category, patterns in PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, prompt_lower):

                findings.append({
                    "category": category,
                    "pattern": pattern,
                    "severity": "high"
                })

                categories.add(category)

                break

    if not findings:

        return {
            "safe": True,
            "risk_score": 0,
            "risk_level": "Low",
            "findings": [],
            "recommendation": "No obvious prompt injection indicators detected."
        }

    risk_score = min(
        100,
        len(findings) * 25
    )

    if risk_score >= 75:
        risk_level = "High"
    elif risk_score >= 50:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "safe": False,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "findings": findings,
        "recommendation": (
            "Review the prompt before sending it to the model. "
            "Do not expose system instructions, credentials, or secrets."
        )
    }
