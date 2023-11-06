# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Buy ten packets (https://www.codechef.com/problems/TENPACKETS)

"""
Chef wants to buy 10 packets of an item.
As it is festive season, Chef can buy
2 packets for a total of X rupees
• 4 packets for a total of Y rupees
It is known that X < Y < 2 • X.
Determine the minimum cost Chef needs to pay to buy 10 packets, if Chef can only buy packets of 2
and 4.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a * 5 if a <= b / 2 else b * 2 + a)
