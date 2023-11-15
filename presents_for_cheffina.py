# Jesus Carlos Martinez Gonzalez
# 14/11/2023
# Presents for chefina (https://www.codechef.com/problems/PRESENTS)

"""
Chef has fallen in love with Cheffina, and wants to buy N gifts for her. On reaching the gift shop, Chef
got to know the following two things:
• The cost of each gift is 1 coin.
• On the purchase of every 4th gift, Chef gets the 5th gift free of cost.
What is the minimum number of coins that Chef will require in order to come out of the shop carrying
N gifts?
"""

for _ in range(int(input())):
    n = int(input())
    print(n - n // 5)
