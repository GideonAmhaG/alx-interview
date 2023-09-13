#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    funtion for rotating the matrix
    """
    # transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    N = len(matrix)
    for i in range(N//2):
        for j in range(N):
            matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
