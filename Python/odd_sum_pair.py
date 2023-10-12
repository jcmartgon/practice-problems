# Jesus Carlos Martinez Gonzalez
# 11/10/2023
# Odd sum pair (https://www.codechef.com/problems/ODDSUMPAIR)

"""
Chef has 3 numbers A, B and C.
Chef wonders if it is possible to choose exactlytwo numbers out of the three numbers such that their
sum is odd.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if (a + b) % 2 != 0 or (a + c) % 2 != 0 or (b + c) % 2 != 0 else "NO")
