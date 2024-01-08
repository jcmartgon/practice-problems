# Jesus Carlos Martinez Gonzalez
# 07/01/2024
# How many digits do I have (https://www.codechef.com/problems/HOWMANY)

"""
Write a program to obtain a number (N) from the user and display whether the number is a one digit
number, 2 digit number, 3 digit number or more than 3 digit number
"""

l = len(input())

print(l if l in [1, 2, 3] else "More than 3 digits")
