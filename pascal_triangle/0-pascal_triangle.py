#!/usr/bin/python3

''' Function that creates Pascal Triangle '''

def pascal_triangle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]

    previous_triangle = pascal_triangle(n - 1)
    previous_row = previous_triangle[-1]
    current_row = [1]

    for i in range(1, n - 1):
        current_row.append(previous_row[i - 1] + previous_row[i])

    current_row.append(1)
    return previous_triangle + [current_row]

n = 5
result = pascal_triangle(n)
for row in result:
    print(row)

