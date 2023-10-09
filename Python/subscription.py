# Jesus Carlos Martinez Gonzalez
# 08/10/2023
# Subscription (https://www.codechef.com/problems/SUBSCRIBE_)

"""
A new TV streaming service was recently started in Chefland called the Chef-TV.
A group of N friends in Chefland want to buy Chef-TV subscriptions. We know that 6 people can share
one Chef-TV subscription. Also, the cost of one Chef-TV subscription is X rupees. Determine the
minimum total cost that the group of N friends will incur so that everyone in the group is able to use
Chef-TV.
"""

from math import ceil

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(ceil(a / 6) * b)
