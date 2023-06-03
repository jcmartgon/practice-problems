# Jesus Carlos Martinez Gonzalez
# 02/06/2023
# Introduction to sets (https://www.hackerrank.com/challenges/py-introduction-to-sets/problem)

"""
Compute the average of all distinct values passed.
"""


def average(array):
    arr = set(array)
    return sum(arr) / len(arr)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
