# Jesus Carlos Martinez Gonzalez
# 03/10/2023
# Chef and chocolates (https://www.codechef.com/problems/CHEFCHOCO)

"""
Chef wants to gift C chocolates to Botswal on his birthday. However, he has only X chocolates with
him.
The cost of I chocolate is Y rupees.
Find the minimum money in rupees Chef needs to spend so that he can gift C chocolates to Botswal.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print((a - b) * c)
