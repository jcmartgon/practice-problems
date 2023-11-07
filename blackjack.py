# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# Blackjack (https://www.codechef.com/problems/BLACKJACK)

"""
Chef is playing a variant of Blackjack, where 3 numbers are drawn and each number lies between 1 and
IO (with both I and IO inclusive). Chef wins the game when the sum of these 3 numbers is exactly 21.
Given the first two numbers A and B, that have been drawn by Chef, what should be 3-rd number that
should be drawn by the Chef in order to win the game?
Note that it is possible that Chef cannot win the game, no matter what is the 3-rd number. In such
cases, report —1 as the answer.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = 21 - (a + b)
    print(c if c <= 10 else -1)
