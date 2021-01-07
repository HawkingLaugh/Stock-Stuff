from io import SEEK_CUR
import yfinance as yf
from get100TrendUSStock import get100Active
import pandas as pd
import time

f = open('Detail.txt', 'w+')

stk_basic_data = yf.Ticker('AAPL').info
info_columns = list(stk_basic_data.keys())
failList = []
stk_info_df = pd.DataFrame(index = get100Active(), columns=info_columns)
for i in stk_info_df.index:
    try:
        print('Current: ', i)
        info_dict = yf.Ticker(i).info
        columns_included = list(info_dict.keys())
        intersect_columns = [x for x in info_columns if x in columns_included]
        stk_info_df.loc[i,intersect_columns] = list(pd.Series(info_dict)[intersect_columns].values)
        time.sleep(1)
    except :
        print('Failed: ', i)
        continue
stk_info_df.to_csv('result.csv')