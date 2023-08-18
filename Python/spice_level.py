# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# Spice level (https://www.codechef.com/problems/KITCHENSPICE)

"""
Each item in Chefs menu is assigned a spice level from 1 to 10. Based on the spice level, the item is
categorised as:
• MILD: Ifthe spice level is less than 4.
• MEDIUM: If the spice level is greater than equal to 4 but less than 7.
• HOT: Ifthe spice level is greater than equal to 7.
Given that the spice level of an item is X find the category it lies in.
"""

for _ in range(int(input())):
    x = int(input())
    if x < 4:
        print("MILD")
    elif x < 7:
        print("MEDIUM")
    else:
        print("HOT")
