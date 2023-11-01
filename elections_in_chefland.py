# Jesus Carlos Martinez Gonzalez
# 01/09/2023
# Elections in chefland (https://www.codechef.com/problems/ELECTN)

"""
Election season has started in Chefland and the election commission wants to know the count of
eligible voters.
There are N people in Chefland where the age of the i person in Ai.
Given that a person needs to be at least X years old to vote. find the number of eligible voters.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    print(sum(1 for x in lst if x >= b))
