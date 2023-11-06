# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Turbo sort (https://www.codechef.com/problems/TSORT)

"""
Given a list of numbers. you have to sort them in non decreasing order.
"""

lst = []

for _ in range(int(input())):
    lst.append(int(input()))

for x in sorted(lst):
    print(x)
