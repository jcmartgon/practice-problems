# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Battery health (https://www.codechef.com/problems/BTRYHLTH)

"""
Apple considers any iPhone with a battery health of 80% or above, to be in optima/condition.
Given that your iPhone has battery health, find whether it is in optima/ condition.
"""

t = int(input())
for _ in range(t):
    print("YES" if int(input()) >= 80 else "NO")
