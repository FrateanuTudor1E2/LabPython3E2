import numpy as np
def zero_matrix(matrix):
    matrix[np.diag_indices_from(matrix)] = 0

    return matrix


A = np.array([[2, 3, 1],
              [5, 1, 5],
              [1, 7, 2]])

print("The 0 matrix is: \n" + str(zero_matrix(A)), end="\n\n")