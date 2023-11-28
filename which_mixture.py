# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Which mixture (https://www.codechef.com/problems/MIXTURE)

"""
Chef has A units of solid and B units of liquid. He combines them to create a mixture. What kind of
mixture does Chef produce: a solution. a solid, or a liquid?
A mixture is called :
1. A solution if A > 0 and B > 0,
2. A solidif B = 0 or
3. A liquidif A = O
"""


for _ in range(int(input())):
    a, b = map(int, input().split())

    print("Solution" if a and b else "Solid" if a else "Liquid")
