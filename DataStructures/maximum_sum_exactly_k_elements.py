# Jesus Carlos Martinez Gonzalez
# 20/07/2023
# Maximum sum with exactly k elements (https://leetcode.com/problems/maximum-sum-with-exactly-k-elements)

"""
You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:

Select an element m from nums.
Remove the selected element m from the array.
Add a new element with a value of m + 1 to the array.
Increase your score by m.
Return the maximum score you can achieve after performing the operation exactly k times.
"""


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + k * (k - 1) // 2
