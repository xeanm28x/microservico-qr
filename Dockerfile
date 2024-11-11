# microservico_qr/Dockerfile

# Use uma imagem base do Python 3.9
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de requirements para o contêiner
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o contêiner
COPY . .

# Exponha a porta em que o Flask irá rodar (5000)
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
