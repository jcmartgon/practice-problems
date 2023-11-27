# Jesus Carlos Martinez Gonzalez
# 26/11/2023
# Mileage matters (https://www.codechef.com/problems/MILEAGE)

"""
Chef wants to rent a car to travel to his restaurant which is N kilometers away. He can either rent a
petrol car or a diesel car.
One litre of petrol costs X rupees and one litre of diesel costs Y rupees. Chef can travel A kilometers
with one litre of petrol and B kilometers with one litre of diesel.
Chef can buy petrol and diesel in any amount. not necessarily integer. For example, if X = 95, Chef
can buy half a litre of petrol by paying 95/2 = 47.5 rupees.
Which car should the chef rent in order to minimize the cost of his travel?
"""


for _ in range(int(input())):
    distance, petrol_cost, diesel_cost, petrol_performance, diesel_performance = map(
        int, input().split()
    )

    petrol_cost = (distance / petrol_performance) * petrol_cost
    diesel_cost = (distance / diesel_performance) * diesel_cost

    print(
        "DIESEL"
        if diesel_cost < petrol_cost
        else "PETROL"
        if petrol_cost < diesel_cost
        else "ANY"
    )
