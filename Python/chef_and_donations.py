# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Chef and donation (https://www.codechef.com/problems/DNATION)

"""
In a certain month, Chef earned X rupees while Chefina earned Y rupees such that Y > X.
Since they want to end up with exactly the same amount, they decide to donate the difference
between their income to a charity.
Find the amount they donate in the month.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y - x)
