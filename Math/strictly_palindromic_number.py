# Jesus Carlos Martinez Gonzalez
# 29/07/2023
# Strictly palindromic number (https://leetcode.com/problems/strictly-palindromic-number)

"""
An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.
"""


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base(n, base):
            if n == 0:
                return "0"

            based = ""
            while n > 0:
                remainder = n % base
                based = str(remainder) + based
                n //= base

            return based

        def is_palindrome(n):
            l = len(n)

            for i in range(l // 2):
                if n[i] != n[l - 1 - i]:
                    return False

            return True

        for base in range(2, n - 1):
            if not is_palindrome(str(to_base(n, base))):
                return False

        return True
