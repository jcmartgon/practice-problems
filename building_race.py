# Jesus Carlos Martinez Gonzalez
# 12/11/2023
# Building race (https://www.codechef.com/problems/BUILDINGRACE)

"""
Two friends Chef and Chefina are currently on floors A and B respectively. They hear an
announcement that prizes are being distributed on the ground floor and so decide to reach the ground
floor as soon as possible.
Chef can climb down X floors per minute while Chefina can climb down Y floors per minute.
Determine who will reach the ground floor first (ie. floor number O). In case both reach the ground floor
together, print Both.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    chef = a / c
    chefina = b / d
    if chef > chefina:
        print("Chefina")
    elif chef < chefina:
        print("Chef")
    else:
        print("Both")
