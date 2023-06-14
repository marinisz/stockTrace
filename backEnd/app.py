from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from flask import Flask, jsonify, request
from selenium.webdriver.chrome.options import Options
from datetime import datetime


app = Flask(__name__)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
PI = 3.14151614123

@app.route('/<stock>', methods=['GET'])
def hello(stock):
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    data = browser.get(f"https://google.com/search?q={stock}")
    price = ""
    try:
        price = browser.find_element("xpath", '//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]').text
    except: 
        return jsonify("NotFound")
    browser.quit()
    data = {
        'stock': f'{stock}',
        'price': price,
        'time': datetime.now().strftime("%H:%M:%S")
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()