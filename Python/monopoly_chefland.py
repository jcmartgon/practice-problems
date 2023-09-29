# Jesus Carlos Martinez Gonzalez
# 28/09/2023
# Monopoly in chefland (https://www.codechef.com/problems/MONOPOLY)

"""
Chef is the financial incharge of Chefland and one of his duties is identifying if any company has gained
a monopolistic advantage in the market.
There are exactly 3 companies in the market each of whose revenues are denoted by RI, R2 and R3
respectively. A company is said to have a monopolistic advantage if its revenue is strictly greater than
the sum of the revenues of its competitors.
Given the revenue of the 3 companies, help Chef determine if any of them has a monopolistic
advantage.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a + b < c or a + c < b or b + c < a else "NO")
