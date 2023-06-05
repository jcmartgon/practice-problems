# Jesus Carlos Martinez Gonzalez
# 04/06/2023
# Exceptions (https://www.hackerrank.com/challenges/exceptions/problem)

"""
You are given two values a and b.
Perform integer division and print a/b.
"""

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        try:
            a = int(a)
        except ValueError:
            print(f"Error Code: invalid literal for int() with base 10: '{a}'")
            continue
        try:
            b = int(b)
        except ValueError:
            print(f"Error Code: invalid literal for int() with base 10: '{b}'")
            continue
        try:
            print(f"{a//b}")
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
