# cython: language_level=3
import numpy as np
cimport numpy as np
import time

# Define numpy data types for Cython
np.import_array()

def cy_matrix_multiplier(np.ndarray[np.float64_t, ndim=2] matrix1, 
                        np.ndarray[np.float64_t, ndim=2] matrix2):
    """
    Cython implementation of matrix multiplication
    """
    cdef:
        int i, j, k
        double dot_prod
        int rows1, cols1, rows2, cols2
        np.ndarray[np.float64_t, ndim=2] result_matrix
    
    # Get matrix dimensions
    rows1 = matrix1.shape[0]
    cols1 = matrix1.shape[1]
    rows2 = matrix2.shape[0]
    cols2 = matrix2.shape[1]
    
    # Check if matrices can be multiplied
    if cols1 != rows2:
        print("Matrix multiplication is not possible")
        return None
    
    # Initialize result matrix
    result_matrix = np.empty((rows1, cols2), dtype=np.float64)
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            dot_prod = 0.0
            
            row = matrix1[i, :]
            col = matrix2[:, j]

           
            for k in range(len(row)):
                dot_prod += row[k] * col[k]
            result_matrix[i, j] = dot_prod
    
    return result_matrix 