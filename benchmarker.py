import time
from fastmatrix import matrix_utils, cy_matrix_utils
import numpy as np

A = np.random.rand(500, 500)
print(A)

iterations = 300

start = time.time()
matrix_utils.loop_matrix_square(A, iterations)
print("Python:", time.time() - start, "seconds")

start = time.time()
cy_matrix_utils.loop_matrix_square(A, iterations)
print("Cython:", time.time() - start, "seconds")