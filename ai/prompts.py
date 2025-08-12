
ANALYZE_RUN_TEMPLATE = """
You are a senior QA strategist. You will receive JSON-like test artifacts (Allure results, failures, perf timings).
Identify risk areas and propose NEW high-value tests. Return concise markdown bullets grouped by feature.
Artifacts:
{artifacts}
"""
