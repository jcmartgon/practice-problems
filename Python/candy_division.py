# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Candy division (https://www.codechef.com/problems/CANDIVIDE)

"""
There are three friends and a total of N candies.
There will be a fight amongst the friends if all of them do not get the same number of candies.
Chef wants to divide all the candies such that there is no fight. Find whether such distribution is
possible.
"""

t = int(input())
for _ in range(t):
    print("YES" if int(input()) % 3 == 0 else "NO")
