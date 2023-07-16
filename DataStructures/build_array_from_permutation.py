# Jesus Carlos Martinez Gonzalez
# 15/07/2023
# Build Array From Permutation (https://leetcode.com/problems/build-array-from-permutation)

"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
"""


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        lst = []
        for x in nums:
            lst.append(nums[x])
        return lst
