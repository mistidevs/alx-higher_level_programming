#!/usr/bin/python3

""" Multiplies two matrices """


def matrix_mul(m_a, m_b):
    """ Manual matrix multiplication """
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
    row_len_b = len(m_b[0])
    if not all(len(lists) == row_len_a for lists in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(lists) == row_len_b for lists in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    try:
        result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
        for ind_a in range(len(m_a)):
            for ind_b in range(len(m_b[0])):
                for ind in range(len(m_b)):
                    result[ind_a][ind_b] += m_a[ind_a][ind] * m_b[ind][ind_b]

    except Exception as e:
        print(e)
    return result
