# Jesus Carlos Martinez Gonzalez
# 04/08/2023
# Audible range (https://www.codechef.com/problems/AUDIBLE)

"""
Chefs dog binary hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive).
If Chef's commands have a frequency of X Hertz. find whether binary can hear them or not.
"""

t = int(input())
for _ in range(t):
    print("YES" if int(input()) in range(67, 45001) else "NO")
