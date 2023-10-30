# Jesus Carlos Martinez Gonzalez
# 30/10/2023
# Nearest exit (https://www.codechef.com/problems/NEARESTEXIT)

"""
There are two exits in a bus with 100 seats:
• First exit is located beside seat number 1.
• Second exit is located beside seat number 100.
Seats are arranged in a straight line from I to 100 with equal spacing between any 2 adjacent seats.
A passenger prefers to choose the nearest exit while leaving the bus.
Determine the exit taken by passenger sitting on seat X.
"""

for _ in range(int(input())):
    print("LEFT" if int(input()) <= 50 else "RIGHT")
