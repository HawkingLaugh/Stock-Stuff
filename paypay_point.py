#%%
import yfinance as yf
import matplotlib.pyplot as plt
import time

plt.ion()
plt.subplots_adjust(hspace=0.5)

while True:
    try:
        SPXL = yf.download(tickers = "SPXL", period = '1d', interval = '1m')
        MYMF = yf.download(tickers = "MYM=F", period = '1d', interval = '1m')
        sD2 = SPXL.tail(30)['Open']
        mD2 = MYMF.tail(30)['Open']
        print(sD2.tail(5))
        print('===================================')
        print(mD2.tail(5))

        plt.subplot(2,1,1)
        line1 = sD2.plot(x = 'Datetime', y = 'Open', color = 'r')
        plt.title('SPXL')

        plt.subplot(2,1,2)
        line2 = mD2.plot(x = 'Datetime', y = 'Open', color = 'g')
        plt.title('MYM=F')

        plt.show(block=False)
        plt.pause(1)
        time.sleep(5)
    except :
        print("Error")
        time.sleep(600)
        continue
# %%
