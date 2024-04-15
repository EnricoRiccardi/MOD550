import sys
import os

sys.path.append('../')

from myfirstcode.dater import DataGenerator 

dater = DataGenerator()
dater.load_well()
dater.select_data()
dater.plot_me(legend='Original')

dater.add_noise(level=0.3)
dater.plot_me(legend='With noise')
