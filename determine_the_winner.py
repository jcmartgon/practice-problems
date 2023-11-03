# Jesus Carlos Martinez Gonzalez
# 02/09/2023
# Determine the winner (https://www.codechef.com/problems/WINNERR)

"""
There is a contest containing 2 problems A and B.
2 strong participants P and Q participated in the contest and solved both the problems.
P made AC submissions on problems A and B at time instants PA and PB respectively while Q made
AC submissions on problems A and B at time instants QA and QB.
It is given that the time penalty is the minimum time instant at which a participant has solved both the
problems. Also the participant with the lower time penalty will have a better rank.
Determine which participant got the better rank or if there is a TIE.
"""

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    p = max(lst[:2])
    q = max(lst[2:])
    if p < q:
        print("P")
    elif q < p:
        print("Q")
    else:
        print("TIE")
