# Jesus Carlos Martinez Gonzalez
# 21/11/2023
# Cost of groceries (https://www.codechef.com/problems/KITCHENCOST)

"""
Chef visited a grocery store for fresh supplies. There are N items in the store where the t item has a
freshness value Ai and cost Bi.
Chef has decided to purchase all the items having a freshness value greater than equal to X. Find the
total cost of the groceries Chef buys.
"""


for _ in range(int(input())):
    n, freshness_threshold = map(int, input().split())
    fresh_values = [int(x) for x in input().split()]
    costs = [int(x) for x in input().split()]

    print(
        sum(
            costs[i] for i, val in enumerate(fresh_values) if val >= freshness_threshold
        )
    )
