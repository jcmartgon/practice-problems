# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Good investment or not (https://www.codechef.com/problems/INVESTMENT)

"""
Chef has invested his money at an interest rate of X percent per annum while the current inflation rate
is Y percent per annum.
An investment is called goodif and only if the interest rate of the investment is at least twice of the
inflation rate.
Determine whether the investment made by Chef is good or not.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print("YES" if x >= y * 2 else "NO")
