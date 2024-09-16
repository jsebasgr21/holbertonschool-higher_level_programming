#!/usr/bin/python3
""" a function that divides all elements of a matrix. """

def matrix_divided(matrix, div):
    """ function that divides the integer or float numbers
    of a matrix"""

    if not isinstance (div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, list) for num in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lenght = len(matrix[0])
    for row in matrix:
        if len(row) != row_lenght:
            raise TypeError("Each row of the matrix must have the same size")

    return[[round(num/div, 2) for num in row] for row in matrix]