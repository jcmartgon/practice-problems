# Jesus Carlos Martinez Gonzalez
# 07/06/2023
# Set Add (https://www.hackerrank.com/challenges/py-set-add/problem)

"""
Find the total number of distinct country stamps.
"""

if __name__ == "__main__":
    n = int(input())
    print(len({input() for _ in range(n)}))
