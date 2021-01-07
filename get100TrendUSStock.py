import pandas as pd

f = open('Most Active 100.txt', 'w+')
def get100Active():
    url = 'https://finance.yahoo.com/screener/predefined/most_actives?offset=0&count=100'
    symbolList = []
    data = pd.read_html(url)[0]
    stk_list = data.Symbol
    Volume_list = data.Volume
    f.write('Symbol, Volume')
    f.write('\n')
    for i,j in zip(stk_list,Volume_list):
        symbolList.append(i)
        str = i + ' ' + j
        f.write(str)
        f.write('\n')
    return symbolList

get100Active()