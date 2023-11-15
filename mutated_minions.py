# Jesus Carlos Martinez Gonzalez
# 15/11/2023
# mutated minions (https://www.codechef.com/problems/CHN15A)

"""
Gru has not been in the limelight for a long time and is, therefore, planning something particularly
nefarious. Frustrated by his minions' incapability which has kept him away from the limelight, he has
built a transmogrifier — a machine which mutates minions.
Each minion has an intrinsic characteristic value (similar to our DNA). which is an integer. The
transmogrifier adds an integer K to each of the minions' characteristic value.
Gru knows that if the new characteristic value of a minion is divisible by 7. then it will have Wolverine-
like mutations.
Given the initial characteristic integers of N minions, all of which are then transmogrified, find out how
many of them become Wolverine-like.
"""


for _ in range(int(input())):
    n, k = map(int, input().split())

    values = list(map(lambda x: x + k, list(map(int, input().split()))))

    print(sum(1 for x in values if x % 7 == 0))
