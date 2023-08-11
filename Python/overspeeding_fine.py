# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Overspeeding fine (https://www.codechef.com/problems/FINE)

"""
Chef was driving on a highway at a speed of X km/hour.
To avoid accidents, there are fine imposed on overspeeding as follows:
• No fine if the speed of the car 70 km/hour.
• Rs 500 fine if the speed of the car is strictly greater than 70 and 100.
• Rs 2000 fine if the speed of the car is strictly greater than 100.
Determine the fine Chef needs to pay.
"""

for _ in range(int(input())):
    x = int(input())
    if x < 71:
        print(0)
    elif x < 101:
        print(500)
    else:
        print(2000)
