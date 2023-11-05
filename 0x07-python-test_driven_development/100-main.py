#!/usr/bin/python3
matrix_mul = __import__('100-mat_mul').matrix_mul

matrixA = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
matrixB = [[1, 2, 3], [4, 5, 6]]

print(matrix_mul(matrixB, matrixA))
print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul())
