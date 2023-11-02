#!/usr/bin/python3

""" Divides all the elements in a matrix """


def matrix_divided(matrix, div):
    """ Divides all elements in a matrix """
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    mat_len = len(matrix)
    divided = [[] for _ in range(mat_len)]

    for row_index, row in enumerate(matrix):
        for index, elem in enumerate(row):
            divided[row_index].append(round(elem / div, 2))

    return divided
