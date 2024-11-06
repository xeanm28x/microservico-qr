# Usar a imagem base do Python
FROM python:3.11-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . .

# Adicionar variáveis de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expor a porta 5000
EXPOSE 5000

# Criar um usuário não-root (boa prática para segurança)
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Comando para rodar a aplicação
CMD ["python", "-m", "flask", "run"]
