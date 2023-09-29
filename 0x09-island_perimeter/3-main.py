#!/usr/bin/python3
"""
Test
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0],
        [0],
        [0]
    ]
    print(island_perimeter(grid))
