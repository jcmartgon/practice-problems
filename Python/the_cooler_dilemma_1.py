# Jesus Carlos Martinez Gonzalez
# 10/10/2023
# The cooler dilemma 1 (https://www.codechef.com/problems/WATERCOOLER1)

"""
Summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool.
He has two options available:
• Rent a cooler at the cost of X coins per month.
• Purchase a cooler for Y coins.
Given that the summer season will last for M months in Chefland, help Chef in finding whether he
should rent the cooler or not.
Chef rents the cooler only if the cost of renting the cooler is strictly less than the cost of purchasing it.
Otherwise, he purchases the cooler.
Print YES if Chef should rent the cooler, otherwise print NO.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a * c < b else "NO")
