import numpy as np
import matplotlib.pyplot as plt


# Generate synthetic data
def generate_linear_synthetic_data(n_random_points):

    x = np.random.rand(n_random_points) * 16

    # We know the truth
    true_slope,  true_intercept = 2, 5
    
    # Give me noise
    y = true_slope * x + true_intercept + np.random.randn(100)  
    
    return x, y

n_random_points = 666
plt.scatter(x, y, color='blue', label='Data Points')

def l_s_method(x, y):
    
# Calculate slope (m) and intercept (b) using least squares method
# m = (N Σ(xy) - Σx Σy) / (N Σ(x^2) - (Σx)^2)
# b = (Σy - m Σx) / N
    n_points = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x*y)
    sum_x2 = np.sum(x**2)

m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / N

# Print the slope and intercept
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Plot the data and the best-fitting line
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, m*x + b, color='red', label='Best-fitting Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression using Least Squares')
plt.legend()
plt.show()

