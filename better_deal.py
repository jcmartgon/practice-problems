# Jesus Carlos Martinez Gonzalez
# 30/10/2023
# Better deal (https://www.codechef.com/problems/BETDEAL)

"""
There are 2 stores in Chefland and both sell the same product. The first store sells the product for 100
rupees whereas the second store sells it for 200 rupees.
It is the holiday season and both stores have announced a special discount. The first store is providing
a discount of A percent on its product and the second store is providing a discount of B percent on its
product.
Chef is wondering which store is selling the product at a cheaper price after the discount has been
applied. Can you help him identify the better deal?
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    a = 100 - a * 1
    b = 200 - b * 2
    if a > b:
        print("SECOND")
    elif a < b:
        print("FIRST")
    else:
        print("BOTH")
