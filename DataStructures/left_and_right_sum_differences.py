# Jesus Carlos Martinez Gonzalez
# 16/07/2023
# Left and right sum differences (https://leetcode.com/problems/left-and-right-sum-differences)

"""
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.
"""


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = [0]
        l = len(nums) - 1

        for i in range(l):
            left_sum.append(left_sum[-1] + nums[i])
            right_sum.insert(0, right_sum[0] + nums[l - i])

        return [abs(a - b) for a, b in zip(left_sum, right_sum)]
