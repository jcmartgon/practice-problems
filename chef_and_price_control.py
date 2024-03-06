# Jesus Carlos Martinez Gonzalez
# 04/03/2024
# Chef and price control (https://www.codechef.com/problems/PRICECON)

"""
Chef has N items in his shop (numbered 1 through N): for each valid i the price of the i-th item is Pi.
Since Chef has very loyal customers, all N items are guaranteed to be sold regardless of their price.
However, the government introduced a price ceiling K. which means that for each item i such that
Pi > K, its price should be reduced from Pi to K.
Chef's revenue is the sum of prices of all the items he sells. Find the amount of revenue which Chef
loses because of this price ceiling.
"""

for _ in range(int(input())):
    n, price_cap = map(int, input().split())
    costs = [int(x) for x in input().split()]
    lost = 0

    for cost in costs:
        if cost > price_cap:
            lost += cost - price_cap

    print(lost)
