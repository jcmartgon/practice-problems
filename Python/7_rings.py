# Jesus Carlos Martinez Gonzalez
# 27/10/2023
# 7 rings (https://www.codechef.com/problems/SEVENRINGS)

"""
In Chefland, a valid phone number consists of 5 digits with no leading zeros.
For example, 98765, 10000, and 71023 are valid phone numbers while 04123, 9231, and 872310 are
not.
Chef went to a store and purchased N items, where the cost of each item is X.
Find whether the total bill is equivalent to a valid phone number.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if len(str(a * b).lstrip("0")) == 5 else "NO")
