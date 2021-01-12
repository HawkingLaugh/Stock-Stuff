from os import sep
import yfinance as yf
import pandas
import matplotlib.pyplot as plt
import time

# to turn the plt into interactive mode for updating 
plt.ion()
while True:
    try:
        while True:
            data = yf.download(tickers="SPXL", period = '5d', interval= '1m')
            d2 = data.tail(5)
            d3raw = data.tail(1)
            d3raw.to_csv('SPXL.csv', header=False, index=True,sep='\t',mode='a')
            d4 = data.tail(30)['Open']
            print(d2)
            line = d4.plot(x = 'Datetime', y = 'Open')
            # plt.annotate('Current', line)
            plt.show(block=False)
            plt.pause(1)
            time.sleep(30)
    except :
        print("Error")
        time.sleep(600)
        continue