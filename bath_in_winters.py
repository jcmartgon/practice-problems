# Jesus Carlos Martinez Gonzalez
# 04/09/2023
# Bath in winters (https://www.codechef.com/problems/BATH)

"""
A geyser has a capacity of X litres of water and a bucket has a capacity of Y litres of water.
One person requires exactly 2 buckets of water to take a bath. Find the maximum number of people
that can take bath using water from one completely filled geyser..
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a // (b * 2))
