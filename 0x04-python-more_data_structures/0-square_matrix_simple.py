#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = [list() for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x = matrix[i][j] ** 2
            mat[i].append(x)
    return mat

if __name__ == '__main__':
    square_matrix_simple()
