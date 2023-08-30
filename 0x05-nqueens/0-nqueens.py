#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard. Write a program that solves the N queens problem.
    Usage: nqueens N
    If the user called the program with the wrong number of arguments,
    print Usage: nqueens N, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new
    line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4, followed by a new
    line, and exit with the status 1
    The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module
"""


import sys


def is_valid(board, row, col, n):
    """
    Check if it's valid to place a queen at board[row][col].
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def n_queens(board, row, n):
    """
    Solve the N queens problem using backtracking.
    """
    if row == n:
        # All queens have been placed on the board.
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_valid(board, row, col, n):
            # Place a queen at this position.
            board[row] = col
            # Recursively solve the rest of the board.
            n_queens(board, row + 1, n)
            # Remove the queen from this position to backtrack.
            board[row] = -1


if __name__ == "__main__":
    # Parse command line arguments.
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty board and solve the N queens problem.
    board = [-1] * n
    n_queens(board, 0, n)
