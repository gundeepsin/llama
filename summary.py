from binance.client import Client
import config
from binance.enums import *

def summary(client):
    #client = Client(config.API_KEY,config.API_SECRET)
    print(client.get_asset_balance(asset='ETH'))
    print(client.get_asset_balance(asset='BTC'))
    print(client.get_asset_balance(asset='USDT'))



