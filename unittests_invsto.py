import unittest
from datetime import datetime
import pandas as pd

excel_file_path = "HINDALCO_1D.xlsx"

df = pd.read_excel(excel_file_path)

def returnCloseTypeAsString(i):
     return str(type(df['close'].values[i]))

def returnOpenTypeAsString(i):
     return str(type(df['open'].values[i]))

def returnLowTypeAsString(i):
     return str(type(df['low'].values[i]))

def returnHighTypeAsString(i):
     return str(type(df['high'].values[i]))

def returnDateTimeTypeAsString(i):
     return str(type(df['datetime'].values[i]))

def returnVolumeTypeAsString(i):
     return str(type(df['volume'].values[i]))
class DataFrameTest(unittest.TestCase):
    def test_data_types(self):
        for i in range(len(df.index)):

            self.assertEqual(returnCloseTypeAsString(i), "<class 'numpy.float64'>")
            self.assertEqual(returnOpenTypeAsString(i), "<class 'numpy.float64'>")
            self.assertEqual(returnLowTypeAsString(i), "<class 'numpy.float64'>")
            self.assertEqual(returnHighTypeAsString(i), "<class 'numpy.float64'>")
            self.assertEqual(returnDateTimeTypeAsString(i), "<class 'numpy.datetime64'>")
            self.assertEqual(returnVolumeTypeAsString(i), "<class 'numpy.int64'>")




        


if __name__ == '__main__':
    unittest.main()

