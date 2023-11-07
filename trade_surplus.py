# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# Trade surplus (https://www.codechef.com/problems/SURPLUS)

"""
Chefland consists of three countries named A, B, and C.
• Country A exports goods worth A1 units and imports goods worth A2 units.
• Country B exports goods worth Bl units and imports goods worth B2 units.
A trade surplus occurs when a country exports strictly more than it imports.
Find whether country C is in trade surplus.
Note that the countries A, B, C trade only between themselves.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("YES" if a - b + c - d < 0 else "NO")
