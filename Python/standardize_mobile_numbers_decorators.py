# Jesus Carlos Martinez Gonzalez
# 29/06/2023
# Standardize Mobile Numbers Using Decorators (https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem)

"""
Let's dive into decorators! You are given N mobile numbers. Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx
"""


def wrapper(f):
    def fun(l):
        formatted_numbers = [
            "+91 " + number[-10:-5] + " " + number[-5:] for number in l
        ]
        f(formatted_numbers)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep="\n")


if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
