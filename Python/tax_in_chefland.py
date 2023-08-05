# Jesus Carlos Martinez Gonzalez
# 04/08/2023
# Tax in chefland (https://www.codechef.com/problems/TAXES)

"""
In Chefland. a tax of rupees 10 is deducted if the total income is strictly greater than rupees 100.
Given that total income is X rupees, find out how much money you get.
"""

t = int(input())
for _ in range(t):
    x = int(input())
    print(x - 10 if x > 100 else x)
