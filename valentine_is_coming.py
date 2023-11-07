# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# Valentine is coming (https://www.codechef.com/problems/VALENTINE)

"""
Valentine's Day is approaching and thus Chef wants to buy some chocolates for someone special.
Chef has a total of X rupees and one chocolate costs Y rupees. What is the maximum number of
chocolates Chef can buy?
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a // b)
