# Jesus Carlos Martinez Gonzalez
# 16/07/2023
# How many numbers are smaller than the current number? (https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number)

"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(1 for x in nums if x < num) for num in nums]
