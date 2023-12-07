# Jesus Carlos Martinez Gonzalez
# 05/12/2023
# Which division (https://www.codechef.com/problems/WHICHDIV)

"""
Given the rating R of a person, tell which division he belongs to. The rating range for each division are
given below:

- Division 1: 2000 Rating.
- Division 2: 1600 Rating < 2000.
- Division 3: Rating < 1600.
"""

for _ in range(int(input())):
    rating = int(input())

    print(3 if rating < 1600 else 2 if rating < 2000 else 1)
