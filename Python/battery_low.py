# Jesus Carlos Martinez Gonzalez
# 25/09/2023
# Battery Low (https://www.codechef.com/problems/BATTERYLOW)

"""
Chef's phone shows a Battery Low notification if the battery level is 15% or less.
Given that the battery level of Chefs phone is determine whether it would show a Battery low
notification.
"""

for _ in range(int(input())):
    print("Yes" if int(input()) <= 15 else "No")
