# Jesus Carlos Martinez Gonzalez
# 28/08/2023
# Profit increment (https://www.codechef.com/problems/PROINC)

"""
Chef recently started selling a special fruit.
He has been selling the fruit for X rupees (X is a multiple of 100). He earns a profit of Y rupees on
selling the fruit currently.
Chef decided to increase the selling price by 10%. Please help him calculate his new profit after the
increase in selling price.
Note that only the selling price has been increased and the buying price is same.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(int(a * 1.1 - (a - b)))
