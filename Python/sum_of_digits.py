# Jesus Carlos Martinez Gonzalez
# 11/09/2023
# Sum of digits (https://www.codechef.com/problems/FLOW006)

"""
You're given an integer N. Write a program to calculate the sum of all the digits of N.
"""

T = int(input())
for i in range(T):
    num = int(input())
    sum = 0
    for j in str(num):
        sum += int(j)
    print(sum)
