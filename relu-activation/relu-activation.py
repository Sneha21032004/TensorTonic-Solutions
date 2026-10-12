import numpy as np

def relu(x):
    x = np.asarray(x, dtype=float)
    return np.array(np.maximum(0.0, x))