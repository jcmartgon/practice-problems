# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Equal distribution (https://www.codechef.com/problems/EQUALDIST)

"""
Alice and Bob are very good friends and they always distribute all the eatables equally among
themselves.
Alice has A chocolates and Bob has B chocolates. Determine whether Alice and Bob can distribute all
the chocolates equally among themselves.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    equi_diff = (y - x) // 2
    print("YES" if x + equi_diff == y - equi_diff else "NO")
