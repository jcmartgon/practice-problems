# Jesus Carlos Martinez Gonzalez
# 19/07/2023
# Check if two string arrays are equivalent (https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent)

"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
