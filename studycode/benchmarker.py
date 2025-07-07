import numpy as np
import time


class MatrixOp:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
    
    def make_random_matrices(self):
        self.matrix1 = np.random.rand(self.num_rows, self.num_cols)
        self.matrix2 = np.random.rand(self.num_cols, self.num_rows)
        print(f"Matrix1 is {self.matrix1}")
        print(f"Matrix2 is {self.matrix2}")

    def matrix_multiplier(self):
        dot_prod=0

        if self.matrix1.shape[1] == self.matrix2.shape[0]: #If true, these are conformable for multiplication
            
            result_matrix = np.empty((self.matrix1.shape[0], self.matrix2.shape[1])) # initialize the resultant array shape
            print(result_matrix.shape)

            for i in range(result_matrix.shape[0]): # 0, 1
                for j in range(result_matrix.shape[1]): # 0, 1
                    
                    row = self.matrix1[i, :]
                    col = self.matrix2[:, j]

                    for k in range(len(row)):
                        dot_prod += row[k]*col[k] #dot product of the vectors(row of A and col of B)

                    result_matrix[i][j] = dot_prod #populate the correct location on the resulting matrix
                    dot_prod=0 #reset 
            print(result_matrix)
            return result_matrix
        else:
            print("Matrix multiplication is not possible")
            return None

    def benchmark_multiplication(self, iterations=100):
        """
        Benchmark custom multiplication vs numpy multiplication
        """
        print(f"\n=== Matrix Multiplication Benchmark ({iterations} iterations) ===")
        print(f"Matrix sizes: {self.matrix1.shape} x {self.matrix2.shape}")
        
        # Time custom implementation
        start_time = time.time()
        for _ in range(iterations):
            custom_result = self.matrix_multiplier()
        custom_time = time.time() - start_time
        
        # Time numpy implementation
        start_time = time.time()
        for _ in range(iterations):
            numpy_result = np.dot(self.matrix1, self.matrix2)
        numpy_time = time.time() - start_time
        
        # Verify results are the same
        if custom_result is not None:
            is_correct = np.allclose(custom_result, numpy_result, rtol=1e-10)
            print(f"\nResults match: {is_correct}")
        
        # Print performance comparison
        print(f"\nCustom implementation: {custom_time:.4f} seconds")
        print(f"Numpy implementation:  {numpy_time:.4f} seconds")
        print(f"Speedup: {custom_time/numpy_time:.2f}x slower than numpy")
        
        return custom_time, numpy_time

newinstance = MatrixOp(300, 300)
newinstance.make_random_matrices()
# Run the benchmark
newinstance.benchmark_multiplication(iterations=10)  # Start with fewer iterations for testing




    
# class MatrixOperations:
#     def __init__(self, A:np.ndarray, B:np.ndarray)-> np.ndarray:
#         self.A = A
#         self.B = B

    # def multiply_matricies(self):
    #     for i in range(np.shape(self.A)[0]):
    #         for j in range(np.shape(self.A)[1]):


# R = [1, 2, 3, 4]
#print(len(R))

# C = [5, 6, 7, 8]
#print(C[0])


# def dot(R, C):
#     RC=0
#     if len(R) == len(C):
#         for i in range(len(R)):
#             RC += (R[i]*C[i])
#             print(RC)
#         return RC
#     else:
#         print("Arrays must have equal length")
# print(dot(R,C))


# matrix1 = np.array([[2, -1, 0], [4, 3, -2]])
#print(matrix1.shape[1])

# matrix2 = np.array([[-4, 0], [6, -4], [1, 6]])
#print(matrix2.shape[0])









                
