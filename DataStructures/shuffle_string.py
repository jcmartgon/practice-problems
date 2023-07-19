# Jesus Carlos Martinez Gonzalez
# 18/07/2023
# Shuffle string (https://leetcode.com/problems/shuffle-string)

"""
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = list(s)

        for i, j in enumerate(indices):
            shuffled[j] = s[i]

        return "".join(shuffled)
