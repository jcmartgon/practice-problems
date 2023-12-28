# Jesus Carlos Martinez Gonzalez
# 27/12/2023
# Inside the stadium (https://www.codechef.com/problems/INSTDUM)

"""
Shubman Gill is playing an international match.
He played a total of N balls, where, in the ball, he scored Ai runs.
no. of runs
x 100.
The strike rate of a player is calculated as :
Preet, a math enthusiast is currently watching the match. Help him find the number of times,
Shubman's strike rate became exactly 100.
"""

for _ in range(int(input())):
    balls_played = int(input())
    runs = [int(run) for run in input().split()]

    total = 0
    counter = 0

    for i, run in enumerate(runs):
        total += run

        if total / (i + 1) * 100 == 100:
            counter += 1

    print(counter)
