# Jesus Carlos Martinez Gonzalez
# 22/11/2023
# Paper cutting (https://www.codechef.com/problems/CUTPAPER)

"""
Chef has a square-shaped chart paper with the side length equal to N. He wants to cut out K x K
squares from this chart paper.
Find the maximum number of K x K squares he can cut from the entire chart paper.
Note that, some part of the chart paper might not be a included in any K x K cutout square.
"""


for _ in range(int(input())):
    n, k = map(int, input().split())
    x = n // k

    print(x * x)
