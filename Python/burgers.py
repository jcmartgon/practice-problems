# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# Burgers (https://www.codechef.com/problems/BURGERS)

"""
Chef is fond of burgers and decided to make as many burgers as possible.

Chef has A patties and B buns. To make 1 burger, Chef needs 1 patty and 1 bun. Find the maximum number of burgers that Chef can make.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x if x < y else y)
