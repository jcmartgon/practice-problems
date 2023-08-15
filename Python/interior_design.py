# Jesus Carlos Martinez Gonzalez
# 14/08/2023
# Interior design (https://www.codechef.com/problems/INTRDSGN)

"""
Chef decided to redecorate his house, and now needs to decide between mro different styles of interior
design.
For the first style, tiling the floor will cost X1 rupees and painting the walls will cost YI rupees.
For the second style, tiling the floor will cost X2 rupees and painting the walls will cost Y2 rupees.
Chef will choose whichever style has the lower total cost. How much will Chef pay for his interior
design?
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(min(a + b, c + d))
