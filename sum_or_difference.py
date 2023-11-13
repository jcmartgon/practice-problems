# Jesus Carlos Martinez Gonzalez
# 12/11/2023
# Sum or difference (https://www.codechef.com/problems/DIFFSUM)

"""
Write a program to take two numbers as input and print their difference if the first number is greater
than the second number otherwise print their sum.
"""

a, b = map(int, input().split())
print(a - b if a > b else a + b)
