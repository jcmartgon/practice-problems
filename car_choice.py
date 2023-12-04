# Jesus Carlos Martinez Gonzalez
# 04/12/2023
# Car choice (https://www.codechef.com/problems/CARCHOICE)

"""
Chef is planning to buy a new car for his birthday. After a long search, he is left with 2 choices:
• Car 1: Runs on diesel with a fuel economy of km/l
• Car 2: Runs on petrol with a fuel economy of km/l
Chef also knows that
• the current price of diesel is YI rupees per litre
• the current price of petrol is Y2 rupees per litre
Assuming that both cars cost the same and that the price of fuel remains constant, which car will
minimize Chefs expenses?
Print your answer as a single integer in the following format
•
•
•
If it is better to choose Car 1, print —1
If both the cars will result in the same expenses. print 0
If it is better to choose Car 2, print 1
"""

for _ in range(int(input())):
    diesel_performance, petrol_performance, diesel_cost, petrol_cost = map(
        int, input().split()
    )

    diesel_cost_efficiency = diesel_cost / diesel_performance
    petrol_cost_efficiency = petrol_cost / petrol_performance

    print(
        -1
        if diesel_cost_efficiency < petrol_cost_efficiency
        else 1
        if petrol_cost_efficiency < diesel_cost_efficiency
        else 0
    )
