# Base Python image
FROM python:3.12-slim

# Ensure stdout/stderr are not buffered
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code
COPY . .

# Entry point: run main.py
CMD ["python", "main.py"]
