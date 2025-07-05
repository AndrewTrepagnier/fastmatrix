# cy_matrix_utils.pyx
def loop_matrix_square(double[:, :] A, int iterations):
    cdef int i, j, k
    cdef int rows = A.shape[0]
    cdef int cols = A.shape[1]
    cdef double[:, :] result = A.copy()

    for k in range(iterations):
        for i in range(rows):
            for j in range(cols):
                result[i, j] = result[i, j] * result[i, j]
    return result
