# Jesus Carlos Martinez Gonzalez
# 10/12/2023
# Chef and contest (https://www.codechef.com/problems/CHEFCONTEST)

"""
Chef and Chefina are competing against each other in a programming contest. They were both able to
solve all the problems in the contest, so the winner between them must be decided by time penalty.
Chef solved all the problems in X minutes and made P wrong submissions, while Chefina solved all
the problems in Y minutes and made Q wrong submissions. Who won the competition (or was it a
draw)?

Note: The time penalty is calculated as follows:

• The base time penalty is the time at which the final problem was solved (so, X for Chef and Y for
Chefina)
• Each wrong submission adds a penalty of 10 minutes
• The winner is the person with less penalty time. If they both have the same penalty, it is considered a
draw.
"""

for _ in range(int(input())):
    chef_time, chefina_time, chef_wrongs, chefina_wrongs = map(int, input().split())

    chef_score = chef_time + chef_wrongs * 10
    chefina_score = chefina_time + chefina_wrongs * 10

    print(
        "Chef"
        if chef_score < chefina_score
        else "Chefina"
        if chefina_score < chef_score
        else "Draw"
    )
