import requests
from pprint import pprint

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']
pprint(data)