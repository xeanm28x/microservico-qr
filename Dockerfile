# Usar a imagem base do Python
FROM python:3.11-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos necessários
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . .

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
