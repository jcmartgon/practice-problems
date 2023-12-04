# Jesus Carlos Martinez Gonzalez
# 04/12/2023
# Total expenses (https://www.codechef.com/problems/FLOW009)

"""
While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than
1000.
If the quantity and price per item are input, write a program to calculate the total expenses.
"""

for _ in range(int(input())):
    quantity, price = map(int, input().split())

    print(quantity * price * 0.9 if quantity > 1000 else quantity * price)
