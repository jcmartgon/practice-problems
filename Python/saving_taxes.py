# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# Saving taxes (https://www.codechef.com/problems/TAXSAVING)

"""
In Chefland, everyone who earns strictly more than Y rupees per year, has to pay a tax to Chef. Chef has allowed a special scheme where you can invest any amount of money and claim exemption for it.

You have earned X (>)(X>Y) rupees this year. Find the minimum amount of money you have to invest so that you don't have to pay taxes this year.
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(x - y)
