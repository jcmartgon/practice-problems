# Jesus Carlos Martinez Gonzalez
# 10/11/2023
# Selling insurance (https://www.codechef.com/problems/AGENTCHEF)

"""
Chef has started a new job as an insurance agent.
Each insurance costs X dollars and Chef gets a 20% commission on selling each insurance.
Find the minimum number of insurances Chef needs to sell to earn at least 100 dollars.
"""

from math import ceil

for _ in range(int(input())):
    print(ceil(100 / (int(input()) * 0.2)))
