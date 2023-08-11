# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Bull or bear (https://www.codechef.com/problems/BULLBEAR)

"""
Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating
whether he made a profit or a loss on his deal.
Given that Chef bought the stock at value X and sold it at value Y. Help him calculate whether he
made a profit, loss, or was it a neutral deal.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        print("LOSS")
    elif y > x:
        print("PROFIT")
    else:
        print("NEUTRAL")
