# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Smallest numbers of notes (https://www.codechef.com/problems/FLOW005)

"""
Consider a currency system in which there are notes of six denominations. namely. Rs. 1. Rs. 2, Rs. 5.
Rs. 10, Rs. 50, Rs. 100.
If the sum of Rs. N is input, write a program to computer smallest number of notes that will combine to
give Rs. N.
"""


for _ in range(int(input())):
    n = int(input())
    min_notes = 0

    denominations = [100, 50, 10, 5, 2, 1]

    for denomation in denominations:
        x = n // denomation
        min_notes += x

        n -= x * denomation

    print(min_notes)
