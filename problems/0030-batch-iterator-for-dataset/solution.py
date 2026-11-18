import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    batches = []
    if y is None:
        return X.tolist()
    num_batches = np.ceil(len(y) / batch_size).astype(int).item()
    for i in range(0, num_batches):
        X_i = X[i*batch_size:(i+1) * batch_size, :]
        y_i = y[i*batch_size:(i+1) * batch_size]
        batches.append([X_i.tolist(), y_i.tolist()])
    return batches