# Jesus Carlos Martinez Gonzalez
# 08/11/2023
# Online or offline (https://www.codechef.com/problems/FOODPLAN)

"""
Chef is confused whether to go out and eat at the restaurant or order food online.
The online order costs N rupees while the cost of eating at the restaurant is M rupees.
However, Chef has a discount coupon with which he can avail flat 10% off on his online order.
Find the cheaper option for Chef to eat, i.e.. whether to order food online or eat at the restaurant.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a * 0.9 > b:
        print("DINING")
    elif a * 0.9 < b:
        print("ONLINE")
    else:
        print("EITHER")
