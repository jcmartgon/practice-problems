# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# The cheaper cab (https://www.codechef.com/problems/CABS)

"""
Chef has to travel to another place. For this, he can avail any one of two cab services.
• The first cab service charges X rupees.
• The second cab service charges Y rupees.
Chef wants to spend the minimum amount of money. Which cab service should Chef take?
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        print("FIRST")
    elif a > b:
        print("SECOND")
    else:
        print("ANY")
