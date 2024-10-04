# Usar uma imagem base do Python
FROM python:3.10

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de requirements para instalar dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação
COPY . .

# Expor a porta que a aplicação irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
