#!/usr/bin/python3
"""
Create a function def island_perimeter(grid): that returns the perimeter of
the island described in grid:

    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to
    the water surrounding the island).
"""


def island_perimeter(grid):
    """
    the aforementioned function
    """
    visit = set()

    def dfs(i, j):
        """
        depth for search function
        """
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or \
                grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0

        visit.add((i, j))
        per = 0
        per = dfs(i, j + 1)
        per += dfs(i + 1, j)
        per += dfs(i, j - 1)
        per += dfs(i - 1, j)
        return per

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
