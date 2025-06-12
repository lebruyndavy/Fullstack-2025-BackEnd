# Dockerfile
FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app

COPY main.py .
COPY database.py .
COPY config.py .
COPY models ./models
COPY queries ./queries
COPY routes ./routes

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
