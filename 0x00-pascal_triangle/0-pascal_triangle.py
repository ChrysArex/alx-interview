#!/usr/bin/python3
"""define the pascal_triangle() function"""


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for idx in range(n - 1):
        row = []
        extended_row = [0, *triangle[idx], 0]
        for e in range(1, len(extended_row)):
            row.append(extended_row[e - 1] + extended_row[e])
        triangle.append(row)
    return triangle
