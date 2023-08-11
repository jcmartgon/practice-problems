# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Final population (https://www.codechef.com/problems/POPULATION)

"""
There were initially X million people in a town, out of which Y million people left the town and Z
million people immigrated to this town.
Determine the final population of town in millions.
"""

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print(x - y + z)
