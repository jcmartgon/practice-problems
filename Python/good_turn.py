# Jesus Carlos Martinez Gonzalez
# 02/08/2023
# Good Turn (https://www.codechef.com/problems/GDTURN)

"""
Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once.

They consider a turn to be good if the sum of the numbers on their dice is greater than 6. Given that in a particular turn Chef and Chefina got X and Y on their respective dice, find whether the turn was good.
"""

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print("YES" if x + y > 6 else "NO")
