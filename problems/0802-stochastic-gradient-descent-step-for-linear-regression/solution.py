import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    n = len(y)

    for step in range(n_iter):
        _i = step % n
        x_i = X[_i]
        y_i = y[_i]
        y_hat = x_i @ weights
        
        error = y_hat - y_i
        grad_w = (2 * error * x_i)

        weights -= learning_rate * grad_w

    return weights.tolist()
