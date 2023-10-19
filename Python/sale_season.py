# Jesus Carlos Martinez Gonzalez
# 18/10/2023
# Sale season (https://www.codechef.com/problems/SALESEASON)

"""
It's the sale season again and Chef bought items worth a total of X rupees. The sale season offer is as
follows:
• if X < 100, no discount.
• if 100 < X 1000, discount is 25 rupees.
• if 1000 < X 5000, discount is 100 rupees.
if X > 5000, discount is 500 rupees.
Find the final amount Chef needs to pay for his shopping.
"""

for _ in range(int(input())):
    x = int(input())
    if x < 100:
        pass
    elif x <= 1000:
        x -= 25
    elif x <= 5000:
        x -= 100
    else:
        x -= 500
    print(x)
