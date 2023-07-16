# Jesus Carlos Martinez Gonzalez
# 15/07/2023
# Number of Good Pairs (https://leetcode.com/problems/number-of-good-pairs)

"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        l = len(nums)

        for i in range(l - 1):
            for j in range(i + 1, l):
                if nums[i] == nums[j]:
                    pairs += 1

        return pairs
