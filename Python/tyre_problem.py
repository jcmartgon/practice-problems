# Jesus Carlos Martinez Gonzalez
# 10/09/2023
# Tyre Problem (https://www.codechef.com/problems/TYRE)

"""
There are N bikes and M cars on the road.
• Each bike has 2 tyres.
• Each car has 4 tyres.
Find the total number of tyres on the road.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a * 2 + b * 4)
