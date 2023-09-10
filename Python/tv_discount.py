# Jesus Carlos Martinez Gonzalez
# 09/09/2023
# TV Discount (https://www.codechef.com/problems/TVDISC)

"""
Chef is looking to buy a TV and has shortlisted two models. The first one costs A rupees. while the
second one costs B rupees.
Since there is a huge sale coming up on Chefzon, Chef can get a flat discount of C rupees on the first
TV, and a flat discount of D rupees on the second one.
Help Chef determine which of the two TVs would be cheaper to buy during the sale.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    first = a - c
    second = b - d
    if first < second:
        print("First")
    elif first > second:
        print("Second")
    else:
        print("Any")
