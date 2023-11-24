# Jesus Carlos Martinez Gonzalez
# 23/11/2023
# Hardest problem bet (https://www.codechef.com/problems/HARDBET)

"""
There are 3 problems in a contest namely A, B, C respectively. Alice bets Bob that problem C is the
hardest while Bob says that problem B will be the hardest.
You are given three integers SA, SB, Sc which denotes the number of successful submissions of the
problems A, B, C respectively. It is guaranteed that each problem has a different number of
submissions. Determine who wins the bet
1. If Alice wins the bet (i.e. problem Cis the hardest), then output Alice.
2. If Bob wins the bet (i.e. problem B is the hardest), then output Bob.
3. If no one wins the bet (i.e. problem A is the hardest). then output Draw.
Note: The hardest problem is the problem with the least number of successful submissions.
"""


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a < b and a < c:
        print("Draw")
    elif b < c:
        print("Bob")
    else:
        print("Alice")
