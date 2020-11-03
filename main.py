# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:46:06 2020

@author: Carlos
"""
import keys
import funciones as f
import datetime
from time import sleep

#binance api
from binance.client import Client

#n-arrays manipulation
import numpy as np


#Codigo

client = Client(keys.APIKey, keys.SecretKey) 

prices = client.get_all_tickers()

symbol= 'BTCUSDT'

klines = f.getDataCurrencyClose(client, symbol, '30m', '29 Oct, 2020')

w = 4
h = 2
priceMatrix = f.getTradingValidationSets(klines, w, h)
print('Input data training:\n')
print(priceMatrix['inputTraining'])
print('\n\n')

print('Output data training\n')
print(priceMatrix['outputTraining'])
print('\n\n')

print('Input data test\n')
print(priceMatrix['inputTest'])
print('\n\n')

print('Output data test\n')
print(priceMatrix['outputTest'])
print('\n\n')


