# Jesus Carlos Martinez Gonzalez
# 08/12/2023
# Relativity (https://www.codechef.com/problems/RELATIVE)

"""
In Chefland, the speed of light is c m/s, and acceleration due to gravity is g m/s2.
Find the smallest height (in meters) from which Chef should jump such that during his journey down
only under the effect of gravity and independent of any air resistance, he achieves the speed of light
and verifies Einstein's theory of special relativity.
Assume he jumps at zero velocity and at any time, his velocity (v) and depth of descent (H) are related
as tp = 2 • g • H.
"""

for _ in range(int(input())):
    gravity, light = map(int, input().split())

    print(int(pow(light, 2) / (2 * gravity)))
