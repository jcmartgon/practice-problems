# Jesus Carlos Martinez Gonzalez
# 17/07/2023
# Decompress run-length encoded list (https://leetcode.com/problems/decompress-run-length-encoded-list)

"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for times, value in zip(nums[::2], nums[1::2]):
            ans.extend([value] * times)

        return ans
