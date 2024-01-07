#!/usr/bin/python3
"""Define a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all element of a matrix.

    Args:
        matrix (list): A list of ints or floats.
        div (int/float): Divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains different sizes of row.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(element, int) or isinstance(element, float))
                for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists"
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
