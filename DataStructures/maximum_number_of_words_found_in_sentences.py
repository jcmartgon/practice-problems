# Jesus Carlos Martinez Gonzalez
# 16/07/2023
# Maximum number of words found in sentences (https://leetcode.com/problems/maximum-number-of-words-found-in-sentences)

"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
"""


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)
