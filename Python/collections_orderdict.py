# Jesus Carlos Martinez Gonzalez
# 06/06/2023
# collections.orderdict (https://www.hackerrank.com/challenges/py-collections-ordereddict/problem)

"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
"""

# The problem was meant as practice for ordered dictionaries but since every dict is now insertion-ordered I just went with a defaultdict instead.

from collections import defaultdict


n = int(input())

items = defaultdict(int)

for _ in range(n):
    item = input().split()
    items[" ".join(item[0:-1])] += int(item[-1])

for item, cost in items.items():
    print(item, cost)
