
FROM mcr.microsoft.com/playwright/python:v1.46.0-jammy
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt && playwright install --with-deps
COPY . .
CMD ["pytest", "-m", "e2e", "-q"]
