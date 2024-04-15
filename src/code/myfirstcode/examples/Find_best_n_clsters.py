import sys
import os
sys.path.append('../')
from myfirstcode.dater import DataGenerator
from myfirstcode.modeller import ModelGenerator

dater = DataGenerator()
dater.load_well()
dater.select_data()
dater.plot_me(legend='Original')

model = ModelGenerator(data=dater.get_data())
model.optimise_k_means(max_k=16)
