# Jesus Carlos Martinez Gonzalez
# 24/11/2023
# Buy 2 get 1 free (https://www.codechef.com/problems/SALE2)

"""
There is a sale going on in Chefland. For every 2 items Chef pays for, he gets the third item for free
(see sample explanations for more clarity).
It is given that the cost of 1 item is X rupees. Find the minimum money required by Chef to buy at
least N items.
"""


for _ in range(int(input())):
    to_buy, cost = map(int, input().split())

    q, r = divmod(to_buy, 3)

    print((r + q * 2) * cost)
