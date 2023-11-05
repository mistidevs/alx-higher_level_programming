#!/usr/bin/python3
import numpy as np


""" Using NumPy to do matrix multiplication """


def lazy_matrix_mul(m_a, m_b):
    """ Matrix multiplication using NumPy """
    if not isinstance(m_a, (list)):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, (list)):
        raise TypeError("m_b must be a list")

    for lists in m_a:
        if not isinstance(lists, list):
            raise TypeError("m_a must be a list of lists")
    for lists in m_b:
        if not isinstance(lists, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if row == []:
            raise ValueError("m_a can't be empty")
    for row in m_b:
        if row == []:
            raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elem in lists:
            if not isinstance(elem, (float, int)):
                raise TypeError("m_a should contain only integers or floats")
    for lists in m_b:
        for elem in lists:
            if not isinstance(elem, (float, int)):
                raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    row_len_b = len(m_a[0])
    if not all(len(lists) == row_len_a for lists in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(lists) == row_len_b for lists in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(np.array(m_a), np.array(m_b))
