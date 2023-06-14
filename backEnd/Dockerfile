# Imagem base do Python
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de código-fonte para o diretório de trabalho
COPY . .

# Instala as dependências do sistema
RUN apt-get update && \
    apt-get install -yq wget unzip libgconf-2-4

# Instala o Chrome
# Instala o Chrome e dependências adicionais
RUN apt-get update && \
    apt-get install -yq wget curl unzip gnupg2 && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -yq google-chrome-stable


# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Define as variáveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expõe a porta do Flask
EXPOSE 5000

# Executa o comando para iniciar a aplicação
CMD ["flask", "run"]
