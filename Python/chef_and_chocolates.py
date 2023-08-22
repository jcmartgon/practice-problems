# Jesus Carlos Martinez Gonzalez
# 21/08/2023
# Chef and chocolates (https://www.codechef.com/problems/CCHOCOLATES)

"""
Chef has X 5 rupee coins and Y 10 rupee coins. Chef goes to a shop to buy chocolates for Chefina
where each chocolate costs Z rupees. Find the maximum number of chocolates that Chef can buy for
Chefina.
"""

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print(int((x * 5 + y * 10) / z))
