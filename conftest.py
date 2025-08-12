
import os, json, time
import pytest
from dotenv import load_dotenv
import allure

load_dotenv()
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(autouse=True)
def _attach_artifacts(request, page):
    start = time.time()
    yield
    duration = time.time() - start
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass
    allure.attach(json.dumps({"duration_sec": round(duration, 3)}), name="perf", attachment_type=allure.attachment_type.JSON)

def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
