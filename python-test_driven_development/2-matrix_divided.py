#!/usr/bin/python3
"""
Module that contains the matrix_divided function.

This function divides all elements of a matrix by a divisor,
with input validations and rounding.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists of floats: New matrix with elements divided by div,
        rounded to 2 decimal places.

    Examples:
        >>> matrix_divided([[1, 2], [3, 4]], 2)
        [[0.5, 1.0], [1.5, 2.0]]
        >>> matrix_divided([[1]], 1)
        [[1.0]]
    """
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if (any(not isinstance(row, list) for row in matrix) or
        any(
            any(not isinstance(ele, (int, float)) for ele in row)
            for row in matrix
        )):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(ele / div, 2) for ele in row]
        new_matrix.append(new_row)

    return new_matrix
