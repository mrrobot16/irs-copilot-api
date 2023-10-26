# Importing necessary libraries
from tensorflow import keras
import numpy as np

# Defining a simple neural network model
model = keras.Sequential([
    keras.layers.Dense(units=2, input_shape=(2,), activation='relu'),
    keras.layers.Dense(units=1, activation='sigmoid')
])

# Compiling the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Displaying the model summary (including initial random weights)
model.summary()

# Setting weights manually for demonstration
weights = [
    np.array([[0.5, 0.2], [-0.5, 0.7]]),  # Weights for the hidden layer
    np.array([0.1, 0.1]),  # Biases for the hidden layer
    np.array([[0.8], [-0.5]]),  # Weights for the output layer
    np.array([0.0])  # Bias for the output layer
]

model.set_weights(weights)

# Making predictions
input_data = np.array([[1, 1]])  # Input data for prediction
predictions = model.predict(input_data)

# Displaying predictions
print(f"Prediction for input {input_data} is: {predictions}")
