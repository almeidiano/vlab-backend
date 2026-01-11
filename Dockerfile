FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies needed by some Python packages
RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev \
	&& rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
	&& pip install --no-cache-dir -r /app/requirements.txt \
	&& pip install --no-cache-dir "uvicorn[standard]"

# Copy application code
COPY . /app

EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

