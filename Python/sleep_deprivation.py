# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Sleep deprivation (https://www.codechef.com/problems/SLEEP)

"""
A person is said to be sleep deprived if he slept strictly less than 7 hours in a day.
Chef was only able to sleep X hours yesterday. Determine if he is sleep deprived or not.
"""

for _ in range(int(input())):
    print("YES" if int(input()) < 7 else "NO")
