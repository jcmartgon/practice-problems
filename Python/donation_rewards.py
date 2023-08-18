# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# Donation rewards (https://www.codechef.com/problems/DOREWARD)

"""
On the occasion of World Blood Donor Day, Chef has organized an event to reward regular blood
donars in Chefland.
• Ifthe donor has made less than or equal to 3 donations, they receive a BRONZE donor badge.
• Ifthe donor has made more than 3 but less than equal to 6 donations, they receive a SILVER donor
badge.
• Ifthe donor has made more than 6 donations, they receive a GOLD donor badge.
Given that a person has made X donations, find the badge they receive.
"""

for _ in range(int(input())):
    x = int(input())
    if x <= 3:
        print("BRONZE")
    elif x <= 6:
        print("SILVER")
    else:
        print("GOLD")
