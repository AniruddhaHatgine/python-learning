import time
import random

def stream_logs():

    price = [200,201,198,199,210,197,204,205,196]
    while True:
        yield random.choice(price)
        time.sleep(1)

def stock_price(price_list):
       for price in price_list:
            if price < 200:
                 yield price

def alert(price_alert):
     for price in price_alert:
          print(f"Price Alert:{price}")

price = stream_logs()
price = stock_price(price)   
alert(price)    


