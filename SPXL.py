import yfinance as yf
import time

while True:
    data = yf.download(tickers="SPXL", period = '5d', interval= '1m')
    d2 = data.tail(5)
    print(d2)
    time.sleep(60)