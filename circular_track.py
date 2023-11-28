# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Circular track (https://www.codechef.com/problems/LOOP)

"""
There is a circular track of length M consisting of M checkpoints and M bidirectional roads such that
each road has a length of I unit. (Like a doubly-linked-list)

Chef is currently at checkpoint A and wants to reach checkpoint B. Find the minimum length of the
road he needs to travel.
"""


for _ in range(int(input())):
    current, goal, total = map(int, input().split())

    print(
        min(abs(goal - current), abs(total - max(goal, current) + min(goal, current)))
    )
