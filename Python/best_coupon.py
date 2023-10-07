# Jesus Carlos Martinez Gonzalez
# 06/10/2023
# Best coupon (https://www.codechef.com/problems/CHEAPFOOD)

"""
Chef is ordering food online (instead of cooking) and the bill comes out to be Rs. X. Chef can use one of
the following two coupons to avail a discount.
• Get 10 percent off on the bill amount
• Get a flat discount of Rs. 100 on the bill amount
What is the maximum discount Chef can avail?
"""

for _ in range(int(input())):
    x = int(int(input()) * 0.10)
    print("100" if x <= 100 else x)
