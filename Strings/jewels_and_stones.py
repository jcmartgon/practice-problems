# Jesus Carlos Martinez Gonzalez
# 24/07/2023
# Jewels and stones (https://leetcode.com/problems/jewels-and-stones)

"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        """
        # No built-ins

        for stone in stones:
            if stone in jewels:
                count += 1
        """

        for jewel in jewels:
            count += stones.count(jewel)

        return count
