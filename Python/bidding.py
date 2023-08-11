# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Bidding (https://www.codechef.com/problems/AUCTION)

"""
Alice, Bob and Charlie are bidding for an artifact at an auction.
Alice bids A rupees, Bob bids B rupees, and Charlie bids C rupees (where A, B, and C are distinct).
According to the rules of the auction, the person who bids the highest amount will win the auction.
Determine who will win the auction.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a > b and a > c:
        print("ALICE")
    elif b > c:
        print("BOB")
    else:
        print("CHARLIE")
