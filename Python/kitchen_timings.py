# Jesus Carlos Martinez Gonzalez
# 05/08/2023
# Kitchen timings (https://www.codechef.com/problems/KITCHENTIME)

"""
The working hours of Chefs kitchen are from X pmto Y pm (I X < Y 12).
Find the number of hours Chef works.
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(y - x)
