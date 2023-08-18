# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# Multivitamin tablets (https://www.codechef.com/problems/TABLETS)

"""
The doctor prescribed Chef to take a multivitamin tablet 3 times a day for the next X days.
Chef already has Y multivitamin tablets.
Determine if Chef has enough tablets for these X days or not.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print("YES" if y >= x * 3 else "NO")
