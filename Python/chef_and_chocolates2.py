# Jesus Carlos Martinez Gonzalez
# 04/10/2023
# Netflix (https://www.codechef.com/problems/NETFLIX)

"""
Alice, Bob, and Charlie are contributing to buy a Netflix subscription. However, Netfix allows only two
users to share a subscription.
Given that Alice, Bob. and Charlie have A, B, and C rupees respectively and a Netflix subscription
costs X rupees, find whether any two of them can contribute to buy a subscription.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("YES" if a + b >= d or a + c >= d or b + c >= d else "NO")
