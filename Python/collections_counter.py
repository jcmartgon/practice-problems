# Jesus Carlos Martinez Gonzalez
# 01/06/2023
# Collections Counter (https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true)

"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""

from collections import Counter

if __name__ == "__main__":
    total = 0
    x = int(input())

    sizes = list(input().split())
    sizes = Counter(sizes)

    n = int(input())
    for _ in range(n):
        size, price = input().split()
        if sizes[size] > 0:
            total += int(price)
            sizes[size] -= 1
    print(total)
