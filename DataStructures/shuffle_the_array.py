# Jesus Carlos Martinez Gonzalez
# 15/07/2023
# Shuffle The Array (https://leetcode.com/problems/shuffle-the-array)

"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = len(nums) // 2
        ans = []

        for i in range(l):
            ans.append(nums[i])
            ans.append(nums[i + l])

        return ans
