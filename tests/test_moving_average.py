from app.moving_average_crossover import moving_average_crossover
import unittest
import pandas as pd

class Testmovingaveragecrossover(unittest.TestCase): # created a class for unit testing mac
    def setUp(self):  #input function for mca
        data={
            'close':[i for i in range(1,151)]
        }
        self.df=pd.DataFrame(data)


    def test_columns_exist(self):
        #test coloumn is added
        result_df = moving_average_crossover(self.df)
        self.assertIn("sma50", result_df.columns)
        self.assertIn("lma100", result_df.columns)
    
    def test_moving_average_values(self):
        #test calculation is coorect
        result=moving_average_crossover(self.df)
        expect_sma=sum(range(1,51))/50
        expect_lma=sum(range(1,101))/100
        self.assertAlmostEqual(result.loc[49,'sma50'],expect_sma,places=2)
        self.assertAlmostEqual(result.loc[99,'lma100'],expect_lma,places=2)


if __name__=="__main__":
     unittest.main()
   
