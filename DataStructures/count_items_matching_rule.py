# Jesus Carlos Martinez Gonzalez
# 18/07/2023
# Count items matching a rule (https://leetcode.com/problems/count-items-matching-a-rule)

"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
"""


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            attr = 0
        elif ruleKey == "color":
            attr = 1
        else:
            attr = 2

        for item in items:
            if item[attr] == ruleValue:
                count += 1

        return count
