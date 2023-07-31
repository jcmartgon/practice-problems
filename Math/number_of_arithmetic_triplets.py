# Jesus Carlos Martinez Gonzalez
# 30/07/2023
# Number of arithmetic triplets (https://leetcode.com/problems/number-of-arithmetic-triplets)

"""
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.
"""


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dic = {}
        quest = {}
        count = 0
        for i in nums:
            dic[i] = True
            if i in quest:
                count += 1
            if i - diff in dic:
                quest[i + diff] = True
        return count
