# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Rain in chefland (https://www.codechef.com/problems/RAINFALL1)

"""
In Chefland, precipitation is measured using a rain gauge in millimetre per hour.
Chef categorises rainfall as:
• LIGHT, if rainfall is less than 3 millimetre per hour.
• MODERATE, if rainfall is greater than equal to 3 millimetre per hour and less than 7 millimetre per
hour.
• HEAVY if rainfall is greater than equal to 7 millimetre per hour.
Given that it rains at X millimetre per hour on a day, find whether the rain is LIGHT. MODERATE, or
HEAVY.
"""

for _ in range(int(input())):
    x = int(input())
    if x < 3:
        print("LIGHT")
    elif x < 7:
        print("MODERATE")
    else:
        print("HEAVY")
