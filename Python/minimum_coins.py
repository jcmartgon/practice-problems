# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# Minimum coins (https://www.codechef.com/problems/MINCOINSREQ)

"""
There are only 2 type of denominations in Chefland:
• Coins worth 1 rupee each
• Notes worth 10 rupees each
Chef wants to pay his friend exactly X rupees. What is the minimum number of coins Chef needs to
pay exactly X rupees?
"""

for _ in range(int(input())):
    print(int(input()) % 10)
