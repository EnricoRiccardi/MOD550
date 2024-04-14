import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Seed for reproducibility
np.random.seed(0)
tf.random.set_seed(0)

# Generate synthetic sine wave data
def generate_sine_wave(timesteps, step=0.1):
    return np.sin(np.arange(0, timesteps * step, step))

# Prepare data for RNN
def prepare_data(data, n_steps):
    X, y = [], []
    for i in range(len(data)):
        end_ix = i + n_steps
        if end_ix > len(data)-1:
            break
        seq_x, seq_y = data[i:end_ix], data[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)

# Define parameters
n_steps = 10
timesteps = 300

# Generate and prepare the data
data = generate_sine_wave(timesteps)
X, y = prepare_data(data, n_steps)
X = X.reshape((X.shape[0], X.shape[1], 1))  # Reshape for RNN [samples, timesteps, features]

# Build the model
model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(n_steps, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

# Train the model
model.fit(X, y, epochs=200, verbose=0)

# Demonstrate prediction
x_input = data[-n_steps:]  # last n_steps from the data
x_input = x_input.reshape((1, n_steps, 1))
yhat = model.predict(x_input, verbose=0)
print(f'Predicted next time point value: {yhat[0][0]}')

# Plot the data and the prediction
plt.plot(np.arange(len(data)), data, label='Sine wave')
plt.scatter(len(data), yhat, color='red', label='Prediction')
plt.legend()
plt.show()

