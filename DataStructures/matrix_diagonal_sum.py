# Jesus Carlos Martinez Gonzalez
# 20/07/2023
# Matrix Diagonal Sum (https://leetcode.com/problems/matrix-diagonal-sum)

"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_sum = 0
        l = len(mat)

        for yi in range(l // 2):
            diagonal_sum += (
                mat[yi][yi]
                + mat[yi][l - 1 - yi]
                + mat[l - 1 - yi][yi]
                + mat[l - 1 - yi][l - 1 - yi]
            )

        q, r = divmod(l, 2)
        if r != 0:
            diagonal_sum += mat[q][q]

        return diagonal_sum
