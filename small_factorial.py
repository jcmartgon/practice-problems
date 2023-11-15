# Jesus Carlos Martinez Gonzalez
# 14/11/2023
# Small factorial (https://www.codechef.com/problems/FLOW018)

"""
Write a program to find the factorial value of any number entered by the user.
"""


def fact(n):
    if n == 0 or n == 1:
        return 1

    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact


for _ in range(int(input())):
    print(fact(int(input())))
