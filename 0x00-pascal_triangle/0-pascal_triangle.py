#!/usr/bin/python3
"""
module for pascal's triangle
"""


def pascal_triangle(n):
    """
    returns pascal's triangle 
    """
    if n <= 0:
        return []
    else:
        p_list = []
        for i in range(n):
            tmp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(p_list[i - 1][j - 1] + p_list[i - 1][j])
            p_list.append(tmp)
        return p_list
