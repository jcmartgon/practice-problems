# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Lunchtime (https://www.codechef.com/problems/LTIME)

"""
Chef has his lunch only between 1 pm and 4 pm (both inclusive).
Given that the current time is X pm, find out whether it is lunchtime for Chef.
"""

for _ in range(int(input())):
    print("YES" if 1 <= int(input()) <= 4 else "NO")
