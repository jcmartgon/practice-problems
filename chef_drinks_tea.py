# Jesus Carlos Martinez Gonzalez
# 31/10/2023
# Chef drinks tea (https://www.codechef.com/problems/TEA)

"""
Chef has planned that he will drink exactly X liters of tea daily. He has an empty jar having a capacity
of Y liters.
Chef can visit the tea shop to refill the jar. In each refill, the jar is completely filled to the brim and Chef
is charged Z rupees.
Chef wonders what is the minimum amount of money he has to pay for drinking exactly X liters of tea
daily.
"""

from math import ceil

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(ceil(a / b) * c)
