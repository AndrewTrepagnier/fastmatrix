import numpy as np

def loop_matrix_square(A, iterations):
    """
    Python implementation of matrix square operation for comparison
    """
    result = A.copy()
    rows, cols = A.shape
    
    for k in range(iterations):
        for i in range(rows):
            for j in range(cols):
                result[i, j] = result[i, j] * result[i, j]
    
    return result 