import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate some sample data
data = np.random.rand(100, 2)  # 100 data points with 2 features

# Define the K-Means clustering model
k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)

# Fit the model to the data
kmeans.fit(data)

# Get the cluster assignments and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot the clustered data
plt.figure(figsize=(8, 6))
for i, color in zip(range(k), ['r', 'g', 'b']):
    plt.scatter(data[labels == i, 0], data[labels == i, 1], c=color, label=f'Cluster {i+1}')

    # Plot the centroid of the current cluster
    plt.scatter(centroids[i, 0], centroids[i, 1], c='black', marker='x', s=100)

plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

