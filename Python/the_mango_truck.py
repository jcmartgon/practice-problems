# Jesus Carlos Martinez Gonzalez
# 27/09/2023
# The mango truck (https://www.codechef.com/problems/MANGOES)

"""
You are given that a mango weighs X kilograms and a truck weighs Y kilograms. You want to cross a
bridge that can withstand a weight of Z kilograms.
Find the maximum number of mangoes you can load in the truck so that you can cross the bridge
safely.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print((c - b) // a)
