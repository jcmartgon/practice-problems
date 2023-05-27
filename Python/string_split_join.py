# Jesus Carlos Martinez Gonzalez
# 27/05/2023
# String split and join (https://www.hackerrank.com/challenges/python-string-split-and-join/problem)

"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""


def split_and_join(line):
    lst = line.split(" ")
    return "-".join(lst)


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
