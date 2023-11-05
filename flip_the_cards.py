# Jesus Carlos Martinez Gonzalez
# 04/09/2023
# Flip the cards (https://www.codechef.com/problems/FLIPCARDS)

"""
There are N cards on a table, out of which X cards are face-up and the remaining are face-down.
In one operation, we can do the following:
• Select any one card and flip it (i.e. if it was initially face-up, after the operation, it will be face-down
and vice versa)
What is the minimum number of operations we must perform so that all the cards face in the same
direction (i.e. either all are face-up or all are face-down)?
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    a -= b
    print(min(a, b))
