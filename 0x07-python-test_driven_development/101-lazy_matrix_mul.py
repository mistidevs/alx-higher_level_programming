#!/usr/bin/python3
import numpy as np


""" Using NumPy to do matrix multiplication """


def lazy_matrix_mul(m_a, m_b):
    """
    Matrix multiplication using NumPy
    Yap it is what is key
    """
    try:
        a = np.array(m_a)
        b = np.array(m_b)
    except ValueError:
        raise ValueError("setting an array element with a sequence.")

    if not (a.ndim == 2 and b.ndim == 2):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if not (a.dtype in (int, float) and b.dtype in (int, float)):
        raise ValueError("invalid data type for einsum")
    if a.size == 0 or b.size == 0:
        raise ValueError("""shapes ({},{}) and ({},{}) not aligned: \
{} (dim 1) != {} (dim 0)""".format(a.shape[0], a.shape[1], b.shape[0],
                                   b.shape[1], a.shape[1], b.shape[0]))
    if a.shape[1] != b.shape[0]:
        raise ValueError("""shapes ({},{}) and ({},{}) not aligned: \
{} (dim 1) != {} (dim 0)""".format(a.shape[0], a.shape[1], b.shape[0],
                                   b.shape[1], a.shape[1], b.shape[0]))

    return np.matmul(a, b)
