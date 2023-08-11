# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Couple game (https://www.codechef.com/problems/COUGAME)

"""
There are G girl and B boy students at IIT (BHIJ) such that B > G.
If ICM were a team game where teams could only be of size 2, having exactly 1 girl student and 1 boy
student, what would be the minimum number of boy students from IIT (BHU) who would not be able
to participate?
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y - x)
