#!/usr/bin/python3
"""Module multiply matrices using NumPy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b"""
    return numpy.matmul(m_a, m_b)
