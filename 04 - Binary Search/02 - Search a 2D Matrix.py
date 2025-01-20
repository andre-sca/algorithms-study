"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
"""

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    first, last = 0, ROWS - 1

    while first <= last:
        middle = (first + last) // 2
        if target > matrix[middle][-1]:
            first = middle + 1
        elif target < matrix[middle][0]:
            last = middle - 1
        else:
            break

    if not (first <= last):
        return False
    row = (first + last) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))

# Time complexity: O(log m + log n)

# Space complexity: O(1)