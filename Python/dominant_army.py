# Jesus Carlos Martinez Gonzalez
# 01/10/2023
# Dominant army (https://www.codechef.com/problems/DOMINANT)

"""
In the medieval age, there were 3 kingdoms A B, and C. The army of these kingdom had NA. NB. and
Nc soldiers respectively.
You are given that an army with X soldiers can defeat an army with Y soldiers only if X > Y.
An army is said to be dominant if it can defeat both the other armies combined. For example,
kingdom Cs army will be dominant only if Nc > NA + NB.
Determine whether any of the armies is dominant or not.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a > b + c or b > a + c or c > a + b else "NO")
