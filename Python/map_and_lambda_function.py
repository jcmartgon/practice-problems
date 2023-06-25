# Jesus Carlos Martinez Gonzalez
# 24/06/2023
# Map and Lambda Function (https://www.hackerrank.com/challenges/map-and-lambda-expression/problem)

"""
Create a function which, given an int N, returns a list of the elements of the fibonacci sequence, from 0 to n - 1.
Then print a list made up of the squares of the previously mentioned one.
"""

cube = lambda x: x**3


def fibonacci(n):
    fibos = [0, 1]
    for _ in range(2, n):
        fibos.append(fibos[-1] + fibos[-2])
    return fibos[:n]


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
