# Jesus Carlos Martinez Gonzalez
# 02/03/2024
# Chef and pairing slippers (https://www.codechef.com/problems/CHEFSLP)

"""
Chef has N slippers, Lof which are left slippers and the rest are right slippers. Slippers must always be
sold in pairs, where each pair contains one left and one right slipper. If each pair of slippers cost X
rupees, what is the maximum amount of rupees that Chef can get for these slippers?
"""

for _ in range(int(input())):
    total, lefts, cost = map(int, input().split())

    print(min(lefts, total - lefts) * cost)
