# Jesus Carlos Martinez Gonzalez
# 03/12/2023
# Vacation transportation (https://www.codechef.com/problems/CHEFTRANS)

"""
Vacations have arrived and Chef wants to go to his home in ChefLand. There are uo types of routes he
can take:
• Take a flight from his college to ChefArina which takes X minutes and then take a bus from
ChefArina to ChefLand which takes Y minutes.
• Take a direct train from his college to ChefLand which takes Z minutes.
Which of these two options is faster?
"""

for _ in range(int(input())):
    flight_time, bus_time, train_time = map(int, input().split())
    planebus_time = flight_time + bus_time

    print(
        "PLANEBUS"
        if planebus_time < train_time
        else "TRAIN"
        if planebus_time > train_time
        else "EQUAL"
    )
