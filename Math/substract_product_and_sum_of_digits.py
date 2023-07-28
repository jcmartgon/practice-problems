# Jesus Carlos Martinez Gonzalez
# 27/07/2023
# Subtract the product and sum of the digits in an integer(https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer)

"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_int = [int(x) for x in str(n)]
        prod = sum = n_int[0]

        for x in n_int[1:]:
            prod *= x
            sum += x

        return prod - sum
