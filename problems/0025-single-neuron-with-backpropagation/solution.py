import numpy as np

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):

    mse_values = []
    updated_weights = initial_weights.astype(float)
    updated_bias = float(initial_bias)
    n = len(labels)

    for _ in range(epochs):
        # Forward
        logits = features @ updated_weights + updated_bias
        sigmoid_values = 1 / (1 + np.exp(-logits))

        # MSE
        epoch_mse_value = np.round(((sigmoid_values - labels) ** 2).mean(), 4)
        mse_values.append(epoch_mse_value)

        # Backprop
        error = sigmoid_values - labels
        sigmoid_der = sigmoid_values * (1 - sigmoid_values)
        delta = 2 * error * sigmoid_der

        grad_w = (features.T @ delta) / n
        grad_b = delta.mean()

        updated_weights -= learning_rate * grad_w
        updated_bias    -= learning_rate * grad_b        
    
    return np.round(updated_weights, 4), np.round(updated_bias, 4), mse_values