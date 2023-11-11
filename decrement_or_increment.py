# Jesus Carlos Martinez Gonzalez
# 10/11/2023
# Decrement or increment (https://www.codechef.com/problems/DECINC)

"""
Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4
otherwise decrement its value by 1.
"""

n = int(input())
print(n + 1 if n % 4 == 0 else n - 1)
