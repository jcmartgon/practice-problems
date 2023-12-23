# Jesus Carlos Martinez Gonzalez
# 22/12/2023
# Chef on vacation (https://www.codechef.com/problems/CHEFVACATION)

"""
After a very long time. the Chef has a vacation. Chef has planned for two trips during this vacation - one
with his family and the other with his friends. The family trip will take X days and the trip with friends
will take Y days. Currently, the dates are not decided but the vacation will last only for Z days.
Chef can be in at most one trip at any time and once a trip is started. Chef must complete it before the
vacation ends. Will Chef be able to go on both these trips if he chooses the dates optimally?
"""

for _ in range(int(input())):
    family_days, friend_days, holidays = map(int, input().split())

    print("YES" if family_days + friend_days <= holidays else "NO")
