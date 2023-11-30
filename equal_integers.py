# Jesus Carlos Martinez Gonzalez
# 29/11/2023
# Equal integers (https://www.codechef.com/problems/INCREAR)

"""
Chef has two integers X and Y. Chefwantsto perform some operations to make X and Y equal. In
one operation, Chef can either:
• set
• or set Y Y +2
Find the minimum number of operations required to make X and Y equal.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    operations = 0

    while x > y:
        y += 2
        operations += 1

    print(operations + y - x)
