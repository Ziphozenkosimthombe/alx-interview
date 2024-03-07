#!/usr/bin/python3

"""creating the triangle function call def pascal_triangle(n):
     - take an integer "n" as input and returns a list representing the first "n" rows of Pascal's triangle
    """

def pascal_triangle(n):
    """checking if "n" is less than or equal to 0.
    - will return the empty list
    """
    if n <= 0:
        return []
    """else the function will initialize a list "triangle" """
    triangle = [[1]]

    """iteratingfrom the second row up to "n"th row
    -- and return the triangle"""
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle
