# Jesus Carlos Martinez Gonzalez
# 15/07/2023
# Concatenation Of Array (https://leetcode.com/problems/concatenation-of-array)

"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums * 2
