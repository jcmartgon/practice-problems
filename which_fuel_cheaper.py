# Jesus Carlos Martinez Gonzalez
# 01/03/2024
# Which fuel is cheaper (https://www.codechef.com/problems/CHEAPFUEL)

"""
The current price of petrol is X rupees, and the current price of diesel is Y rupees. At the start of each
month, the price of petrol increases by A rupees and the price of diesel increases by B rupees.
Chef is curious to know which fuel costs less at the end of the Kth month. If petrol is cheaper than
diesel at the end of Kth month, then print PETROL. If diesel is cheaper than petrol at the end of the
Kth month, then print DIESEL. If both the fuels have the same price at the end of the Kth month, then
print SAME PRICE.
"""

for _ in range(int(input())):
    petrol_cost, diesel_cost, petrol_increase, diesel_increase, months = map(
        int, input().split()
    )

    petrol_cost += petrol_increase * months
    diesel_cost += diesel_increase * months

    print(
        "PETROL"
        if petrol_cost < diesel_cost
        else "DIESEL" if petrol_cost > diesel_cost else "SAME PRICE"
    )
