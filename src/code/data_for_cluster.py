import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
data = np.random.rand(100, 2)  # 100 data points with 2 features

plt.scatter(data[:, 0], data[:, 1])
plt.show()
