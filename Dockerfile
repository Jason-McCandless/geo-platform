FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Why each part matters

# FROM python:3.11-slim

# Small, production-friendly base image

# WORKDIR /app

# Everything runs from here (predictability)

# COPY requirements.txt → install deps

# Docker layer caching (faster rebuilds)

# CMD uvicorn ... 0.0.0.0

# Critical: allows traffic into container

# This is a classic gotcha you just avoided

# To build and run:
# docker compose up --build