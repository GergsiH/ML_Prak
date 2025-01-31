import numpy as np

def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    unique_x, counts_x = np.unique(x, return_counts=True)
    unique_y, counts_y = np.unique(y, return_counts=True)
    return np.array_equal(unique_x, unique_y) and np.array_equal(counts_x, counts_y)

def max_prod_mod_3(x: np.ndarray) -> int:
    products = x[1:] * x[:-1]
    valid_products = products[products % 3 == 0]
    return int(valid_products.max()) if valid_products.size > 0 else -1

def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    weighted_sum = image * weights[None, None, :]
    return np.sum(weighted_sum, axis=2)

def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    expanded_x = np.repeat(x[:, 0], x[:, 1])
    expanded_y = np.repeat(y[:, 0], y[:, 1])
    
    if expanded_x.size != expanded_y.size:
        return -1
    return int(np.dot(expanded_x, expanded_y))

def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    X_norm = np.linalg.norm(X, axis=1, keepdims=True)  # n x 1
    Y_norm = np.linalg.norm(Y, axis=1, keepdims=True)  # m x 1

    X_mask = X_norm.flatten() == 0
    Y_mask = Y_norm.flatten() == 0
    
    X_norm[X_mask] = 1
    Y_norm[Y_mask] = 1

    M = X @ Y.T / (X_norm * Y_norm.T)

    M[X_mask, :] = 1  
    M[:, Y_mask] = 1  

    return M