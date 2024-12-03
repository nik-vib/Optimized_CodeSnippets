import numpy as np
import time

def naive_matrix_multiply(A, B):
    """
    Naive implementation of matrix multiplication
    Time complexity: O(n^3)
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError("Matrix dimensions are incompatible for multiplication")
    
    result = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                result[i, j] += A[i, k] * B[k, j]
    
    return result

def optimized_numpy_multiply(A, B):
    """
    Highly optimized matrix multiplication using NumPy
    Leverages BLAS (Basic Linear Algebra Subprograms)
    """
    return np.dot(A, B)

def strassen_matrix_multiply(A, B):
    """
    Strassen's algorithm for matrix multiplication
    Time complexity: O(n^2.807)
    Efficient for large matrices
    """
    # Base case for small matrices
    if A.shape[0] <= 64 or A.shape[1] <= 64:
        return np.dot(A, B)
    
    # Pad matrices to power of 2 size if needed
    def pad_matrix(X):
        n = X.shape[0]
        m = X.shape[1]
        next_power_of_two = 2 ** int(np.ceil(np.log2(max(n, m))))
        padded = np.zeros((next_power_of_two, next_power_of_two))
        padded[:n, :m] = X
        return padded

    # Pad matrices if needed
    A_padded = pad_matrix(A)
    B_padded = pad_matrix(B)
    n = A_padded.shape[0]

    # Base case
    if n <= 64:
        return np.dot(A, B)

    # Divide matrices
    mid = n // 2
    a11 = A_padded[:mid, :mid]
    a12 = A_padded[:mid, mid:]
    a21 = A_padded[mid:, :mid]
    a22 = A_padded[mid:, mid:]

    b11 = B_padded[:mid, :mid]
    b12 = B_padded[:mid, mid:]
    b21 = B_padded[mid:, :mid]
    b22 = B_padded[mid:, mid:]

    # Compute Strassen's 7 matrix multiplications
    p1 = strassen_matrix_multiply(a11 + a22, b11 + b22)
    p2 = strassen_matrix_multiply(a21 + a22, b11)
    p3 = strassen_matrix_multiply(a11, b12 - b22)
    p4 = strassen_matrix_multiply(a22, b21 - b11)
    p5 = strassen_matrix_multiply(a11 + a12, b22)
    p6 = strassen_matrix_multiply(a21 - a11, b11 + b12)
    p7 = strassen_matrix_multiply(a12 - a22, b21 + b22)

    # Compute result quadrants
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 - p2 + p3 + p6

    # Combine results
    result = np.zeros((n, n))
    result[:mid, :mid] = c11
    result[:mid, mid:] = c12
    result[mid:, :mid] = c21
    result[mid:, mid:] = c22

    # Trim to original matrix size
    return result[:A.shape[0], :B.shape[1]]

def benchmark_matrix_multiplication():
    """
    Benchmark different matrix multiplication methods
    """
    print("Matrix Multiplication Benchmark:")
    sizes = [100, 500, 1000]
    
    for size in sizes:
        A = np.random.rand(size, size)
        B = np.random.rand(size, size)
        
        print(f"\nMatrix Size: {size}x{size}")
        
        # Naive method
        start = time.time()
        naive_matrix_multiply(A, B)
        naive_time = time.time() - start
        print(f"Naive Method Time: {naive_time:.4f} seconds")
        
        # NumPy method
        start = time.time()
        optimized_numpy_multiply(A, B)
        numpy_time = time.time() - start
        print(f"NumPy Method Time: {numpy_time:.4f} seconds")
        
        # Strassen method
        start = time.time()
        strassen_matrix_multiply(A, B)
        strassen_time = time.time() - start
        print(f"Strassen Method Time: {strassen_time:.4f} seconds")

# Uncomment to run benchmark
benchmark_matrix_multiplication()