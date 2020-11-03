# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:00:11 2020

@author: Carlos
"""

#n-arrays manipulation
import numpy as np

#binance api
from binance.client import Client

#Funciones

#Obtener los datos OHLC de una moneda
def getDataCurrency(client, symbol, interval, start_str, end_str=None):
    klines = client.get_historical_klines(symbol,interval, start_str, end_str)
    klines = np.array(klines)
    klines = klines[:,0:6] #Nos quedamos con los valores Timestamp, Open, High, Low, Close, Volume
    return klines




#Obtener los datos de Close de una moneda
def getDataCurrencyClose(client, symbol, interval, start_str, end_str=None):
    klines = client.get_historical_klines(symbol,interval, start_str, end_str)
    klines = np.array(klines)
    klines = klines[:,4] #Nos quedamos con el valor Close
    return klines




#Dividir priceMatrix en los conjuntos inputTraining, outputTraining, inputTest y outputTest
#Devuelve un diccionario {inputTraining, outputTraining, inputTest, outputTest}

def trainingValidationPartition(priceMatrix):
    sizeTraining = len(priceMatrix['input']) * 70 / 100
    sizeTraining = round(sizeTraining)
    sizeTest = len(priceMatrix['input']) - sizeTraining
    
    inputTraining = priceMatrix['input'][:sizeTraining]
    inputTest = priceMatrix['input'][sizeTraining:sizeTest+sizeTraining]
    
    outputTraining = priceMatrix['output'][:sizeTraining]
    outputTest = priceMatrix['output'][sizeTraining:sizeTest+sizeTraining]
    
    return {'inputTraining':inputTraining, 'outputTraining':outputTraining, 'inputTest':inputTest, 'outputTest':outputTest }




#A partir de los precios y las ventanas de tamaño w y h, obtener una priceMatrix
#Devuelve un diccionario {inputTraining, outputTraining, inputTest, outputTest}

def getTradingValidationSets(prices, w, h):
    
    prices = np.array(prices)
    priceMatrix = {'input': np.arange(w), 'output': np.arange(h)}
    
    i = 0
    while i < prices.size - w -h + 1:
        auxInput = w + i
        auxOutput = auxInput + h
        
        rowInput = prices[i:auxInput]
        rowOutput = prices[auxInput: auxOutput]
        
        priceMatrix['input'] = np.vstack((priceMatrix['input'], rowInput))
        priceMatrix['output'] = np.vstack((priceMatrix['output'], rowOutput))
        
        i+=1
    
    priceMatrix['input'] = priceMatrix['input'][1:priceMatrix['input'].size, :]
    priceMatrix['output'] = priceMatrix['output'][1:priceMatrix['output'].size, :]
    
    priceMatrix = trainingValidationPartition(priceMatrix)
    
    return priceMatrix