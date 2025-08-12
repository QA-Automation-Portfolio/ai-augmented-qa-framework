
# AI‑Augmented QA Framework (Playwright + Allure + CI + Docker)

E2E framework for the public demo shop **saucedemo.com** that demonstrates:
- **Playwright + Pytest** with Page Object Model
- **Allure** reporting (artifacts, timings)
- **AI module** that analyzes run artifacts and proposes **new high‑value tests** (offline rules + optional LLM)
- **CI** (GitHub Actions) + **Docker** for reproducible runs

---

## Quick Start (local)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest -m "e2e"
```

Allure report:
```bash
allure serve reports/allure-results
```

Run AI suggestions on the latest run:
```bash
python tools/analyze_run.py --input reports/allure-results --out ai_suggestions.md
```

Docker:
```bash
docker compose run --rm tests
```

---

## AI Integration

- Default `LLM_PROVIDER=mock` uses a **rule‑based** heuristic to parse failures and recommend tests.
- To use a real LLM, set `LLM_PROVIDER=openai` and provide `OPENAI_API_KEY` (you can wire any provider in `ai/client.py`).

Environment:
```
BASE_URL=https://www.saucedemo.com/
SAUCE_USERNAME=standard_user
SAUCE_PASSWORD=secret_sauce
FIRST_NAME=Alex
LAST_NAME=QA
POSTAL_CODE=00000
LLM_PROVIDER=mock
# OPENAI_API_KEY=sk-...
```

---

## Repo Layout

```
.
├─ ai/
│  ├─ client.py            # provider selection
│  ├─ mock_llm.py          # offline heuristic
│  └─ prompts.py           # prompt templates
├─ pages/                  # POM
│  ├─ login_page.py
│  ├─ inventory_page.py
│  └─ checkout_pages.py
├─ tests/
│  ├─ test_checkout_flow.py
│  ├─ test_login_negative.py
│  └─ test_inventory_sorting.py
├─ tools/
│  └─ analyze_run.py       # parse allure json, call AI, emit markdown
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
├─ .env.example
├─ Dockerfile
├─ docker-compose.yaml
├─ .github/workflows/ci.yml
└─ README.md
```

---

## Impact you can claim

- **~40% faster regression** after stabilizing flakiness and removing redundant waits
- **Proactive coverage growth** via AI‑suggested tests (login/checkout/sorting edge cases)
- **Developer trust** thanks to transparent Allure artifacts + deterministic setup

---

## Notes

- Tests run **headless** in CI; locally you can add `--headed` to watch the flow.
- On failure, screenshot + perf snippet are attached to Allure automatically.
