import unittest
import sys
import os

sys.path.append('../')

from myfirstcode.dater import DataGenerator


class MyDataTest(unittest.TestCase):
    def test_datar_init(self):
        dataclass = DataGenerator()
        self.assertTrue(type(dataclass), 'class')  # add assertion here

    def test_datar_load_well(self):
        dataclass = DataGenerator()
        path = os.path.abspath('.')
        if os.path.exists('tests'):
            path = os.path.abspath('tests')
        filename = 'xeek_train_subset_mini.csv'
        dataclass.load_well(data_file=os.path.join(path, '..',  filename))
        print(dataclass.df['DEPTH_MD'].iloc[1])
        self.assertTrue(dataclass.df['DEPTH_MD'].iloc[1] == 439.56778984)


if __name__ == '__main__':
    unittest.main()
