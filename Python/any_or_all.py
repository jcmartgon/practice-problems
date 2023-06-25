# Jesus Carlos Martinez Gonzalez
# 22/06/2023
# Any or All (https://www.hackerrank.com/challenges/any-or-all/problem)

"""
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
"""

if __name__ == "__main__":
    n = int(input())
    ints = input().split()
    print(all(int(x) > 0 for x in ints) and any(x == x[::-1] for x in ints))
