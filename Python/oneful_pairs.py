# Jesus Carlos Martinez Gonzalez
# 16/08/2023
# Oneful pairs (https://www.codechef.com/problems/ONEFULPAIRS)

"""
Chef defines a pair of positive integers (a, b) to be a Oneful Pair. if
a + b + (a. b) = 111
For example, (I, 55) is a Oneful Pair, since I + 55 + (I • 55) = 56 + 55 = III.
But (1, 56) is not a Oneful Pair, since 1 + 56 + (1 • 56) = 57 + 56 = 113 111.
Given two positive integers a and b, output Yes if they are a Oneful Pair. And No otherwise.
"""

a, b = map(int, input().split())
print("YES" if a + b + a * b == 111 else "NO")
