import buy as b
import sell as s
import summary as su      ##defaulted to ETH because does let you do ETH-PERPETUAL 
import price as p
import logs_ETH_short as lg


import time
import requests
from binance.client import Client
import config
from binance.enums import *
import sys


global currency
global tha_dough   #the amount of USDT we wanna buy or sell
global mark_price
global BREAK_PRICE
global orderId
global diff
global TELE_TOKEN
global chat_id
global ping_pong
global old
global SECONDS
global client
global ping_pong_count

TELE_TOKEN = "6034277983:AAHKdYppG-cw3FBII7wLisDoSbWfw_GwbHo"
TELE_TOKEN2 = "5903882275:AAGApm67fCPcuMHynovZGmS2yMjmQjnQhlM"
chat_id = "5789191868"
chat_id2 = "566644123"
currency = "ETHUSDT"
ping_pong_count = 100000000
BREAK_PRICE = 1000000000
tha_dough = 0
diff = 100000

def main(input1,input2,input3,input4):
    make_values(input1,input2,input3,input4)
    global currency
    global tha_dough   #the amount of USDT we wanna buy or sell
    global mark_price
    global BREAK_PRICE
    global orderId
    global diff
    global TELE_TOKEN
    global chat_id
    global ping_pong
    global old
    global SECONDS
    global client
    global ping_pong_count
    client = Client(config.API_KEY,config.API_SECRET)


    old = time.time()

    ping_pong = 0

    message = "None"

    mark_price = float(p.price( currency))
    old_spice = float(mark_price)

    su.summary(client)
    still = time.time()

    while True: 
        '''YEAR        = datetime.date.today().year     # the current year
        MONTH       = datetime.date.today().month    # the current month
        DATE        = datetime.date.today().day      # the current day
        HOUR        = datetime.datetime.now().hour   # the current hour
        MINUTE      = datetime.datetime.now().minute # the current minute
        #SECONDS     = datetime.datetime.now().second # the current second'''
        SECONDS = time.time()
            
        mark_price = float(p.price( currency))
        #print(mark_price)

        if(SECONDS - old > 1.5):
            five_percent(old_spice)
            old = SECONDS
        

        #lg.logg(mark_price)

        if(ping_pong == ping_pong_count):
            message = f"PING PONG COUNT IS AT {ping_pong}"
            url = f"https://api.telegram.org/bot{TELE_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            url2 = f"https://api.telegram.org/bot{TELE_TOKEN2}/sendMessage?chat_id={chat_id2}&text={message}"
            requests.get(url).json() 
            requests.get(url2).json()
            ping_pong = 0
            sys.exit()

            

        if(float(mark_price) < BREAK_PRICE and float(mark_price) > (BREAK_PRICE - 1) or (float(mark_price) < (BREAK_PRICE - 3))):
            yu = s.sell(client,tha_dough , currency)
            print(yu)
            orderId = yu["orderId"]
            mo = "SHORT INITIATED OF " + str(tha_dough) + " IN CURRENCY  " + currency + " AT " + str(mark_price) + " ORDER ID: " +  str(orderId) + " ETH SHORT BOT"
            lg.logg(mo)
            counter1 = 0
            still1 = SECONDS #sd

            
            message = f"SHORT INITIATED OF {tha_dough} IN CURRENCY {currency} AT {mark_price} ETH SHORT BOT"
            url = f"https://api.telegram.org/bot{TELE_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            url2 = f"https://api.telegram.org/bot{TELE_TOKEN2}/sendMessage?chat_id={chat_id2}&text={message}"
            requests.get(url).json() 
            requests.get(url2).json()

            
            still1 = time.time()
            
            while True:
                #lg.logg(mark_price)
                SECONDS     = time.time() #the current second
                
                mark_price = float(p.price( currency))
                five_percent(old_spice)
                print("MARK PRICE" + str(float(mark_price)) + " STOP LOSS " + str(BREAK_PRICE + diff))
                if(float(mark_price) > (BREAK_PRICE + diff)):
                    yu = b.buy(client,tha_dough, currency)
                    orderId = yu["orderId"]
                    nogh = "SHORT DROPPED OF " + str(tha_dough) + " IN CURRENCY" + currency + " AT " + str(mark_price) + " ETH SHORT BOT"
                    lg.logg(mo)
                    break
            message = f"SHORT DROPPED OF {tha_dough} IN CURRENCY {currency} AT {mark_price} ETH SHORT BOT"
            url = f"https://api.telegram.org/bot{TELE_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            url2 = f"https://api.telegram.org/bot{TELE_TOKEN2}/sendMessage?chat_id={chat_id2}&text={message}"
            requests.get(url).json()
            requests.get(url2).json()
            ping_pong += 1

        else:
            pass



        

def make_values(value1, value2, value3, value4=0):
    global diff
    global BREAK_PRICE
    global mark_price
    global ping_pong_count
    global tha_dough
    global currency

    mark_price = 0

    BREAK_PRICE = float(value1)

    tha_dough = float(value2)

    diff = float(value3)

    ping_pong_count = int(value4)

    print("BREAK PRICE: " + str(BREAK_PRICE) + " THE AMOUNT INVESTED(BTC/ETH): " + str(tha_dough) + " THE DIFFERENCE FOR STOP LOSS IS: " + str(BREAK_PRICE - diff) + "  MARK_PRICE " + str(mark_price))
    #lg.logg(f"BREAK PRICE: {BREAK_PRICE}      THE AMOUNT INVESTED(BTC/ETH): {tha_dough}       THE DIFFERENCE FOR STOP LOSS IS: {diff}")



def five_percent(old_spice):
    global mark_price
    global diff
    global BREAK_PRICE
    global ping_pong_count
    global tha_dough
    global currency
 
    difference = ((old_spice - mark_price)/old_spice) * 100
    old_spice = mark_price
    old = time.time()
    if(difference >= 5 or difference <= -5):
        if(difference >= 5):
            message = f"5% OR MORE HAS RISEN FROM {currency}"
        elif(difference <= -5):
            message = f"5% OR MORE HAS BEEN DROPPED FROM {currency}"
            
        url = f"https://api.telegram.org/bot{TELE_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        url2 = f"https://api.telegram.org/bot{TELE_TOKEN2}/sendMessage?chat_id={chat_id2}&text={message}"
        requests.get(url).json() 
        requests.get(url2).json()
    print("PRICE CHECKED")
    print("BREAK PRICE: " + str(BREAK_PRICE) + " THE AMOUNT INVESTED(BTC/ETH): " + str(tha_dough) + " STOP LOSS IS: " + str(BREAK_PRICE + diff) + "  MARK_PRICE " + str(mark_price))
       


    

    

    
