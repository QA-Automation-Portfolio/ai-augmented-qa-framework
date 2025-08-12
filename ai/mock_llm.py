
import textwrap

def suggest_from_artifacts(text: str) -> str:
    ideas = []
    low = text.lower()
    if "timeout" in low or "timed out" in low:
        ideas.append("• Add retries/backoff and throttled-network tests.")
    if "401" in low or "403" in low:
        ideas.append("• Role/permission matrix; token expiration cases.")
    if "500" in low or "trace" in low:
        ideas.append("• Negative payloads, resilience, idempotency.")
    if "sorting" in low:
        ideas.append("• Parametrize all sort keys in asc/desc.")
    if "checkout" in low:
        ideas.append("• Address/ZIP validation and currency formatting.")
    if "login" in low:
        ideas.append("• Lockout rules, password policy, rate‑limit.")
    if not ideas:
        ideas.append("• Boundary tests for inputs & pagination.")

    return textwrap.dedent("### AI Suggestions (mock)\n" + "\n".join(ideas) + "\n")
