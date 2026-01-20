FROM python:3.11-slim

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala as dependências do container para os pacotes de Python
RUN apt-get update \
	&& apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev \
	&& rm -rf /var/lib/apt/lists/*

# Dependências do uvicorn e fastapi
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
	&& pip install --no-cache-dir -r /app/requirements.txt \
	&& pip install --no-cache-dir "uvicorn[standard]"

# Copia a aplicação pra pasta /app do container e expoe a porta 8000, padrao do fastapi
COPY . /app
EXPOSE 8001

# Executa o fastapi com uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

