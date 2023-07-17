# Jesus Carlos Martinez Gonzalez
# 16/07/2023
# Running sum of 1-d array (https://leetcode.com/problems/running-sum-of-1d-array)

"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [nums[0]]

        for num in nums[1:]:
            running_sum.append(running_sum[-1] + num)

        return running_sum
