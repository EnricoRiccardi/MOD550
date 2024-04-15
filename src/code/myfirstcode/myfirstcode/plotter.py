# https://matplotlib.org/devdocs/devel/testing.html
import seaborn as sns
import matplotlib.pyplot as plt


class PlotterGenerator:
    def __init__(self, description='Plot generator', data=None):
        """Initializes the class creating the required attributes."""
        self.description = description
        self.df = data

    def crossplots(self, dataset, hue='KMEANS'):
        """Creates seaborn pairplot coloured by kmm labels"""
        sns.pairplot(dataset, vars=['GR', 'RHOB', 'NPHI', 'DTC'],
                     hue=hue, palette='Dark2',
                     diag_kind='kde',
                     plot_kws={'s': 15, 'marker': 'o', 'alpha': 1})
        plt.show()


