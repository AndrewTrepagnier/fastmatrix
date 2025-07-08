import numpy as np
cimport numpy as np
import time

def cymultipler(np.ndarray[np.float64_t, ndim=2] matrix1, np.ndarray[np.float64_t, ndim=2] matrix2):  # datatype(size if available) name

    cdef:
        int i
        int j
        int k
        double dot_prod
        int rows1
        int rows2
        int cols1
        int cols2
        np.ndarray[np.float64_t, ndim=2] result_matrix

    
    rows1 = matrix1.shape[0]
    cols1 = matrix1.shape[1]
    rows2 = matrix2.shape[0]
    cols2 = matrix2.shape[1]

    
    if matrix1.shape[1] != matrix2.shape[0]:
        print("Matrix multiplication is not possible")
        return None

    
    result_matrix = np.empty((matrix1.shape[0],matrix2.shape[1]), dtype=np.float64)

    for i in range(rows1):
        for j in range(cols2):
            dot_prod = 0.0
            
            row = matrix1[i, :]
            col = matrix2[:, j]
           
            for k in range(len(row)):
                dot_prod += row[k] * col[k]
            result_matrix[i, j] = dot_prod
    
    return result_matrix 
    

