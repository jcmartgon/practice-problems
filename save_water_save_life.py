# Jesus Carlos Martinez Gonzalez
# 11/01/2024
# Save water save life (https://www.codechef.com/problems/SAVWATER)

"""
To address the situation of Water Scarcity in Chefland, Chef has started an awareness campaign to
motivate people to use greywater for toilets, washing cars. gardening, and many other chores which
don't require the use of freshwater. These activities presently consume y liters of water every week per
household and Chef thinks through this campaign he can help cut down the total usage to ]
Assuming c liters of water every week per household is consumed at chores where using freshwater is
mandatory and a total of C liters of water is available for the entire Chefland having H households for
a week. find whether all the households can now have sufficient water to meet their requirements.
"""

from math import floor

for _ in range(int(input())):
    households, fresh, grey, total = map(int, input().split())

    print("YES" if households * (fresh + floor(grey / 2)) <= total else "NO")
