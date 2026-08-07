# 1. Usa uma imagem oficial estável e leve do Python
FROM python:3.11-slim

# 2. Configurações de ambiente para o Python no Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Define o diretório de trabalho onde o projeto vai rodar dentro do container
WORKDIR /app

# 4. Instala dependências de sistema básicas para compilação (necessárias para o Pillow/Imagens)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia primeiro apenas o arquivo de dependências (otimiza o cache do Docker)
COPY requirements.txt /app/

# 6. Instala as bibliotecas do Python (Django, Pillow, tzdata)
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copia TODO o conteúdo da pasta hugel_manner_plattler para dentro do container
COPY . /app/

# 8. Informa que o container escutará na porta 8000
EXPOSE 8000

# 9. Comando que roda os prepares do banco e inicia o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]