FROM python:3.9-slim

# Install system packages
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    git \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
