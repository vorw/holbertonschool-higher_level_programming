#!/usr/bin/python3
"""
Module that contains the function matrix_divided.

This function divides all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists of floats: New matrix with elements divided by div
                                 and rounded to 2 decimal places.

    Examples:
        >>> matrix = [[1, 2], [3, 4]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0], [1.5, 2.0]]
    """
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(any(not isinstance(ele, (int, float)) for ele in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all rows have the same size
    row_length = len(matrix[0]) if matrix else 0
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Compute new matrix with divided and rounded values
    new_matrix = []
    for row in matrix:
        new_row = [round(ele / div, 2) for ele in row]
        new_matrix.append(new_row)

    return new_matrix
