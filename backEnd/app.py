import os
from selenium import webdriver
from flask import Flask, jsonify, send_from_directory
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

chrome_options = Options()
chrome_options.add_argument("--headless")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='C:\projetosCode\stockTrace\\backEnd\static\\favicon.ico')

@app.route('/<stock>', methods=['GET'])
def hello(stock):
    # Obter o diretório do script atual
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Configurar o caminho para o chromedriver na pasta atual
    chrome_driver_path = os.path.join(script_dir, 'chromedriver.exe')
    service = Service(ChromeDriverManager().install())
    # Configurar o navegador Chrome
    browser = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Visitar a página do Google Finance
        browser.get(f"https://google.com/search?q={stock}")

        # Extrair o preço da ação
        price = browser.find_element("xpath", '//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]').text
    except: 
        # Se não encontrar o elemento, retornar "NotFound"
        return jsonify("NotFound")
    finally:
        # Fechar o navegador
        browser.quit()

    # Construir a resposta JSON
    data = {
        'stock': f'{stock}',
        'price': price,
        'time': datetime.now().strftime("%H:%M:%S")
    }
    return jsonify(data)

if __name__ == '__main__':
    # Iniciar o servidor Flask
    app.run()
