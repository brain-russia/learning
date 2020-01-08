import csv
import datetime
import requests
import pandas as pd

bdbtg = open("BD-Btg.csv", "w")
publicKey = '6F04OgnZYtJXoF0opGAAopfAiP9Dhlax'
secretKey = 'NMmIE3PLj2qg8ltzvxVn3v0tFYs_pe2V'
session = requests.session()
session.auth = (publicKey, secretKey)
c = datetime.datetime(2017, 10, 24, 8, 35, 00, 00)
x = 1
d = c + datetime.timedelta(minutes=5015)
candles= session.get('https://api.hitbtc.com/api/2/public/candles/BTGBTC', params= {'limit': '1000', 'from': c, 'period': 'M5'}).json()
candles_df= pd.DataFrame(candles)

candles_df['timestamp']= pd.to_datetime(candles_df['timestamp'])
candles_df.set_index('timestamp')
print(candles_df)
candles_df.to_csv(bdbtg, index=False, encoding='utf-8')
bdbtg.close()
bdbtg1 = open("BD-Btg.csv", "a")

while x < 232:
    x += 1
    candles2 = session.get('https://api.hitbtc.com/api/2/public/candles/BTGBTC', params= {'limit': '1000', 'from': d, 'period': 'M5'}).json()
    candles2_df = pd.DataFrame(candles2)
    candles2_df['timestamp']= pd.to_datetime(candles2_df['timestamp'])
    candles2_df.set_index('timestamp')
    print(candles2_df)
    candles2_df.to_csv(bdbtg1, index=False, encoding='utf-8', header=False)
    d += datetime.timedelta(minutes=5015)

bdbtg1.close()