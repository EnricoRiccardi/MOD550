import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class DataGenerator:
    def __init__(self, description='Data generator'):
        """Initializes the class creating the required attributes."""
        self.description = description
        self.df = None

    def load_well(self, data_file=None, well_name="16/10-1"):
        """Read a dataset."""
        if data_file is None:
            path = os.path.abspath('../')
            data_file = os.path.join(path, 'xeek_train_subset_mini.csv')
        self.df = pd.read_csv(data_file)
        self.df = self.df[self.df["WELL"] == well_name]  # select data only for the specific well

    def select_data(self, select=['GR', 'RHOB', 'NPHI', 'DTC']):
        self.df = self.df[select].dropna()

    def add_noise(self, properties=("RHOB", "GR"), level=0.1):
        """Adds noise to the data."""
        for prop in properties:
            # RHOB usually varies between 1.9-2.9 g/cm3 wheres GR between 5-300.
            scaled_noise = level if prop == "RHOB" else level*50
            noise = np.random.uniform(low=-scaled_noise, high=scaled_noise, size=len(self.df[prop]))
            self.df[prop] += noise

    def plot_me(self, x_lab='RHOB', y_lab='GR', legend=''):
        """Plots datasets."""
        plt.scatter(self.df[x_lab], self.df[y_lab], label=legend)
        plt.xlabel(x_lab)
        plt.ylabel(y_lab)
        plt.legend()
        plt.show()

    def get_data(self):
        return self.df
