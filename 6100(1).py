import numpy as np
vector = np.array([10, 20, 30, 40, 50, 60])
print("Original Vector: ", vector)

matrix = np.array([[11, 22, 33],
                   [44, 55, 66],
                   [77, 88, 99]])
print("Original Matrix: ", matrix)

V = vector.T
print("Transpose Vector:", V)

M = matrix.T
print("Transpose Matrix:", M)
