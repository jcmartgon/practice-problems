# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# Car trip (https://www.codechef.com/problems/CARTRIP)

"""
Chef rented a car for a day.
Usually, the cost of the car is Rs IO per km. However, since Chef has booked the car for the whole day,
he needs to pay for at least 300 kms even if the car runs less than 300 kms.
If the car ran X kms, determine the cost Chef needs to pay.
"""

for _ in range(int(input())):
    x = int(input()) * 10
    print(x if x > 3000 else 3000)
