import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


class ModelGenerator:
    def __init__(self, description='Model generator', data=None):
        """Initializes the class creating the required attributes."""
        self.description = description
        self.df = data

    def optimise_k_means(self, max_k):
        """Plots number of clusters vs the inertia which helps to determine the optimal number of clusters to be used"""
        # The user can choose to run the original data with no noise or the one with added noise
        means = []
        inertias = []

        # Applies kmeans over a range of different cluster numbers limited by max_k
        for k in range(1, max_k):
            kmeans = KMeans(n_clusters=k, n_init=16)
            kmeans.fit(self.df[["GR", "RHOB"]])
            means.append(k)
            inertias.append(kmeans.inertia_)

        # Plotting parameters
        plt.subplots(figsize=(10, 5))
        plt.plot(means, inertias, 'o-')
        plt.xlabel("Number of Clusters")
        plt.ylabel("Inertia")
        plt.grid(True)
        plt.show()

    def k_means(self, n_clusters):
        """Applies k-mean models."""
        kmeans = KMeans(n_clusters=n_clusters, n_init=16)
        kmeans.fit(self.df)
        self.df['KMEANS'] = kmeans.labels_

    def gmm(self, n_clusters):
        """Applies gmm models."""
        gmm = GaussianMixture(n_clusters)
        gmm.fit(self.df)
        self.df['GMM'] = gmm.predict(self.df)

