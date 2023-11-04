# Jesus Carlos Martinez Gonzalez
# 03/09/2023
# Maximise the tastiness (https://www.codechef.com/problems/MAXTASTE)

"""
Chef is making a dish that consists of exactly two ingredients. He has four ingredients A, B, C and D
with tastiness a, b, c, and d respectively. He can use either A or B as the first ingredient and either C
or D as the second ingredient.
The tastiness of a dish is the sum of tastiness of its ingredients. Find the maximum possible tastiness
of the dish that the chef can prepare.
"""

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    print(max(lst[:2]) + max(lst[2:]))
