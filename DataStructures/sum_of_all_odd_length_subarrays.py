# Jesus Carlos Martinez Gonzalez
# 19/07/2023
# Sum of all odd length subarrays (https://leetcode.com/problems/sum-of-all-odd-length-subarrays)

"""
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
"""


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        l = len(arr)
        lengths = [i for i in range(1, l + 1, 2)]

        for length in lengths:
            for i in range(0, l - length + 1):
                total += sum(arr[i : i + length])

        return total
