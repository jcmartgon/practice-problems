# Jesus Carlos Martinez Gonzalez
# 30/11/2023
# Equal integers (https://www.codechef.com/problems/INCREAR)

"""
Chef has two integers X and Y. Chefwantsto perform some operations to make X and Y equal. In
one operation, Chef can either:

- set x to x + 1
- set y to y + 1

Find the minimum number of operations required to make X and Y equal.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())

    if x > y:
        y_operations = (x - y) // 2
        y += y_operations * 2

        print(y_operations + x - y if x == y else y_operations + x - y + 1)
    else:
        print(y - x)
