"""from binance.client import Client
import config
from binance.enums import *

def price(client,currency):
    #client = Client(config.API_KEY,config.API_SECRET)
    pricee = client.get_symbol_ticker(symbol=currency)
    #pricee = client.get_all_tickers()
    # print full output (dictionary)
    return pricee["price"]#[11]['price']"""

import requests

def price(currency):
    # Make a GET request to the /fapi/v1/premiumIndex endpoint
    response = requests.get('https://fapi.binance.com/fapi/v1/premiumIndex', params={'symbol': currency})

    # Parse the response JSON and extract the mark price
    data = response.json()
    latest_price = data['markPrice']

    # Print the latest mark price to the console
    return latest_price


#print(price(Client(config.API_KEY,config.API_SECRET),"BTCUSDT"))



'''import json
import requests
  
# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  
# requesting data from url
data = requests.get(key)  
data = data.json()
print(f"{data['symbol']} price is {data['price']}")'''