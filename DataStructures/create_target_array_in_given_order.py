# Jesus Carlos Martinez Gonzalez
# 17/07/2023
# Create target array in given order (https://leetcode.com/problems/create-target-array-in-the-given-order)

"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
"""


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i, num in enumerate(nums):
            target.insert(index[i], num)

        return target
