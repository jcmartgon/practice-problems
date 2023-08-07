# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Who is taller? (https://www.codechef.com/problems/TALLER)

"""
Alice and Bob were having an argument about which of them is taller than the other. Charlie got
irritated by the argument and decided to settle the matter once and for all.
Charlie measured the heights of Alice and Bob, and got to know that Alice's height is X centimeters and
Bob's height is Y centimeters. Help Charlie decide who is taller.
It is guaranteed that X Y.
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print("A" if x > y else "B")
