#!/usr/bin/python3
"""Define the perimeter finder function"""


def island_perimeter(grid):
    """
    args:
        grid: the grid defining the islande
    returns:
        the perimeter of the island described in grid
    """
    elements = []
    dem_p1, dem_p2 = 0, 0
    xs, ys, count_x, count_y = [], [], 0, 0
    perimeter, line, column = 0, 1, 1
    for li in grid:
        for co in li:
            if co == 1:
                perimeter += 4
                elements.append((line, column))
                if column not in xs:
                    xs.append(column)
                if line not in ys:
                    ys.append(line)
            column += 1
        column = 1
        line += 1
    following = []
    for x in xs:
        for e in elements:
            if e[1] == x:
                following.append(e)
        for i in range(len(following) - 1):
            if following[i + 1][0] == (following[i][0] + 1):
                count_x += 1
        perimeter -= 2 * count_x
        count_x = 0
        following = []

    following = []
    for y in ys:
        for e in elements:
            if e[0] == y:
                following.append(e)
        for i in range(len(following) - 1):
            if following[i + 1][1] == (following[i][1] + 1):
                count_y += 1
        perimeter -= 2 * count_y
        count_y = 0
        following = []
    return perimeter
