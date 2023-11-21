# Jesus Carlos Martinez Gonzalez
# 20/11/2023
# The cooler dilemma 2 (https://www.codechef.com/problems/WATERCOOLER2)

"""
The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room
cool. He has two options available:
• Rent a cooler at the cost of X coins per month.
• Purchase a cooler for Y coins.
Chef wonders what is the maximum number of months for which he can rent the cooler such that the
cost of renting is strictly less than the cost of purchasing it.
"""


for _ in range(int(input())):
    to_rent, to_buy = map(int, input().split())

    months = to_buy // to_rent

    print(months if months != 1 else 0)
