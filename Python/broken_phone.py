# Jesus Carlos Martinez Gonzalez
# 09/09/2023
# Broken Phone (https://www.codechef.com/problems/BROKENPHONE)

"""
Uttu broke his phone. He can get it repaired by spending X rupees or he can buy a new phone by
spending Y rupees. Uttu wants to spend as little money as possible. Find out if it is better to get the
phone repaired or to buy a new phone.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        print("REPAIR")
    elif a > b:
        print("NEW PHONE")
    else:
        print("ANY")
