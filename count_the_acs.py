# Jesus Carlos Martinez Gonzalez
# 11/11/2023
# Count the acs (https://www.codechef.com/problems/ACS)

"""
There are 10 problems in a contest. You know that the score of each problem is either 1 or 100 points.
Chef came to know the total score of a participant and he is wondering how many problems were
actually solved by that participant.
Given the total score P of the participant, determine the number of problems solved by the
participant. Print —1 in case the score is invalid.
"""

for _ in range(int(input())):
    big, small = divmod(int(input()), 100)
    total = big + small
    print(total if total <= 10 else -1)
