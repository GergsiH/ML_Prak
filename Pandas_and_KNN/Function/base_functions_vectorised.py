import numpy as np


def get_part_of_array(X: np.ndarray) -> np.ndarray:
    every_fourth_row = X[::4, :]

    selected_columns = every_fourth_row[:, 120:500:5]
    
    return selected_columns
    


def sum_non_neg_diag(X: np.ndarray) -> int:
    diag_elements = np.diagonal(X)
    
    non_neg_elements = diag_elements[diag_elements >= 0]
    
    if non_neg_elements.size == 0:
        return -1
    
    return np.sum(non_neg_elements)


def replace_values(X: np.ndarray) -> np.ndarray:
    modified_array = X.copy()
    
    column_means = np.mean(X, axis=0)
    
    for j in range(X.shape[1]): 
        M = column_means[j] 
        modified_array[(modified_array[:, j] < 0.25 * M) | (modified_array[:, j] > 1.5 * M), j] = -1
    
    return modified_array
 
