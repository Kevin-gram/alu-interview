#!/usr/bin/python3

''' Function that creates Pascal Triangle '''


def pascal_triangle(n):

    '''returning empty list if n is less than or equal to 0'''
    if n <= 0:
        return []

    this_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(this_triangle[i-1][j-1] + this_triangle[i-1][j])
        row.append(1)
        this_triangle.append(row)

    return this_triangle
