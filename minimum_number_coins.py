# Jesus Carlos Martinez Gonzalez
# 08/09/2023
# Minimum number of coins (https://www.codechef.com/problems/MINCOINS)

"""
Chef has infinite coins in denominations of rupees 5 and rupees IO.
Find the minimum number of coins Chef needs, to pay exactly X rupees. If it is impossible to pay X
rupees in denominations of rupees 5 and 10 only, print —1.
"""

for _ in range(int(input())):
    x = int(input())

    if x % 10 == 0 or x % 5 == 0:
        tens = x // 10
        print(tens + (x - tens * 10) // 5)
        continue

    print(-1)
