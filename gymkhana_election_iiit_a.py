# Jesus Carlos Martinez Gonzalez
# 03/09/2023
# Gymkhana election IIIT-A (https://www.codechef.com/problems/CS2023_GYM)

"""
In the Gymkhana elections of IIIT-A. N members are nominated for senator positions. The total
number of voters in the college is M.
Om, one of the N nominees, wants to secure a strict majority win in the election.
Assuming all voters cast their votes, find the minimum number of votes Om requires to ensure a strict
majority win.
Note that in a strict majority win all the nominees have strictly lesser votes than the winner.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(b // 2 + 1)
