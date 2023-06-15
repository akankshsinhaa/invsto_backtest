import unittest
from datetime import datetime
import pandas as pd

excel_file_path = "HINDALCO_1D.xlsx"

df = pd.read_excel(excel_file_path)

def returnClose(i):
     return df['close'].values[i]

def returnOpen(i):
     return df['open'].values[i]

def returnLow(i):
     return df['low'].values[i]

def returnHigh(i):
     return df['high'].values[i]

def returnDateTime(i):
     return df['datetime'].values[i]

def returnVolume(i):
     return df['volume'].values[i]