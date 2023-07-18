# Jesus Carlos Martinez Gonzalez
# 17/07/2023
# Sum multiples (https://leetcode.com/problems/sum-multiples)

"""
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0

        for i in range(n + 1):
            if not i % 3 or not i % 5 or not i % 7:
                ans += i

        return ans
