import unittest
import pandas as pd
from app.moving_average_crossover import generate_signal

class Testgeneratesignal(unittest.TestCase):
    def test_generate_signal(self):
      data={
            'sma50': [95, 100, 105, 110, 105],  
            'lma100': [100, 100, 102, 108, 110]
      }
      df=pd.DataFrame(data)
      result_df=generate_signal(df)
      expected=['','buy','','','sell']
      self.assertListEqual(result_df['signal'].to_list(),expected)
