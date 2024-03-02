# Jesus Carlos Martinez Gonzalez
# 01/03/2024
# Existence (https://www.codechef.com/problems/EXISTENCE)

"""
Chef has two variables X and Y. He wants to find out whether the variables satisfy the equation:

X4+4. =4.X2.Y
"""

for _ in range(int(input())):
    x, y = map(int, input().split())

    print("YES" if pow(x, 4) + 4 * pow(y, 2) == 4 * pow(x, 2) * y else "NO")
