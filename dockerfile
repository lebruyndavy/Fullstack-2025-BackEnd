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

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
az ad sp create-for-rbac --name "github-actions-deploy" --role contributor --scopes /subscriptions/2625a888-91cf-4a18-8bbd-db39574ce9d9/resourceGroups/fullstack-2025-backend --sdk-auth
