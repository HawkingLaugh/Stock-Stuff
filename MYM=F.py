from os import sep
import yfinance as yf
import pandas
import time

swtich = 0
while True:
    if swtich == 0:
        swtich = 1
        data = yf.download(tickers="MYM=F", period = '5d', interval= '1m')
        d2 = data.tail(5)
        d3raw = data.tail(1)
        d3raw.to_csv('MYM=F.csv', header=False, index=True,sep='\t',mode='a')
        print(d2)
        time.sleep(30)
    elif swtich == 1:
        swtich = 0
        data = yf.download(tickers="MYM=F", period = '5d', interval= '1m')
        d2 = data.tail(5)
        print(d2)
        time.sleep(30)