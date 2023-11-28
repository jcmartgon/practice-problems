# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Summer heat (https://www.codechef.com/problems/COCONUT)

"""
Chefland has 2 different types of coconut, type A and type B. Type A contains only ca milliliters of
coconut water and type B contains only grams of coconut pulp. Chefs nutritionist has advised him
to consume Xa milliliters of coconut water and Xb grams of coconut pulp every week in the summer.
Find the total number of coconuts (type A + type B) that Chef should buy each week to keep himself
active in the hot weather.
"""

from math import ceil

for _ in range(int(input())):
    a_has, b_has, a_need, b_need = map(int, input().split())

    print(ceil(a_need / a_has) + ceil(b_need / b_has))
