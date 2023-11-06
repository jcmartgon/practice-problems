# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Candy distribution (https://www.codechef.com/problems/CANDYDIST)

"""
Chef has N candies. He has to distribute them to exactly M of his friends such that each friend gets
equal number of candies and each friend gets even number of candies. Determine whether it is
possible to do so.
NOTE: Chef will not take any candies himself and will distribute all the candies.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if (a / b) % 2 == 0 else "NO")
