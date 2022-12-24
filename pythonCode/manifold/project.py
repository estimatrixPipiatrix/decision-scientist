import numpy as np

def random_projection(X,dimension=3,rseed=42):
    assert dimension >= X.shape[1]
    rng = np.random.RandomState(rseed)
    C = rng.randn(dimension, dimension)
    e, V = np.linalg.eigh(np.dot(C,C.T))
    return np.dot(X, V[:X.shape[1]])
