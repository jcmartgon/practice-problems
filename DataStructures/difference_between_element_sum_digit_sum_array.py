# Jesus Carlos Martinez Gonzalez
# 18/07/2023
# Difference between an element sum and a digit sum of an array (https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array)

"""
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.
"""


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        num_sum = sum(nums)
        dig_sum = sum([int(d) for d in "".join(str(num) for num in nums)])

        return abs(num_sum - dig_sum)
