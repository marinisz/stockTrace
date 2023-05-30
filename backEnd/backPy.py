import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=X1PG3T46SAM0TR96'
r = requests.get(url)
data = r.json()

print(data)