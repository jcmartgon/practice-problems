# Jesus Carlos Martinez Gonzalez
# 27/11/2023
# Melt gold (https://www.codechef.com/problems/MELTGOLD)

"""
Chef has an ore with melting point of X degrees.
Chefs kiln has a initial temperature of Y degrees. The temperature of the kiln increases by i degrees
after the i minute.
Find the minimum time in minutes after which the ore starts melting.
Note:
• We are only concerned about the temperature at the end of each minute and not during a minute.
• The ore starts melting if the temperature of the kiln becomes greater than or equal to the melting
point.
"""


for _ in range(int(input())):
    goal, current = map(int, input().split())

    i = 1
    while current + i < goal:
        current += i
        i += 1

    print(i)
