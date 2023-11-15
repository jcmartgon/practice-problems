# Jesus Carlos Martinez Gonzalez
# 15/11/2023
# Buy lamps (https://www.codechef.com/problems/BUYLAMP)

"""
An electronics shop sells red and blue lamps. A red lamp costs X rupees and a blue lamp costs Y
rupees.
Chef is going to buy exactly N lamps from this shop. Find the minimum amount of money Chef needs
to pay such that at least K of the lamps bought are red.
"""


for _ in range(int(input())):
    to_buy, min_reds, red_cost, blue_cost = map(int, input().split())
    print(
        to_buy * red_cost
        if red_cost <= blue_cost
        else min_reds * red_cost + (to_buy - min_reds) * blue_cost
    )
