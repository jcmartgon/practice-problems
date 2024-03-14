# Jesus Carlos Martinez Gonzalez
# 13/03/2024
# Car range (https://www.codechef.com/problems/CARRANGE)

"""
The fuel economyof a car is the distance which it can travel on one litre of fuel.
The base fuel economy (i.e. its fuel economy when there is only one person - the driver - in the car) of a
certain car is M kilometres per litre. It was also observed that every extra passenger in the car
decreases the fuel economy by 1 kilometre per litre.
P people want to take this car for a journey. They know that the car currently has V litres of fuel in its
tank.
What is the maximum distance this car can travel under the given conditions, assuming that all P
people always stay in the car and no refuelling can be done?
Note that among the P people is also a driver, i.e, there are exactly P people in the car.
"""

for _ in range(int(input())):
    people, fuel_economy, litres = map(int, input().split())

    print(litres * (fuel_economy - (people - 1)))
