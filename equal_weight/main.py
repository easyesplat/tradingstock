import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

#replicating a "fake" read-in of stock data
stocks = pd.read_csv('/Users/eric/Desktop/stockBot/tradingstock/equal_weight/sp_500_stocks.csv')
#print(stocks)