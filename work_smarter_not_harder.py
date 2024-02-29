# Jesus Carlos Martinez Gonzalez
# 28/02/2024
# Work smarter not harder (https://www.codechef.com/problems/SMARTER)

"""
The tortoise and the hare decide to run a race, yet again.
This time around however, the hare has gotten a bit smarter!
The racetrack is a straight line, L meters long.
The tortoise moves at VI meters per second, while the hare moves at V2 meters per second. It is
known that VI < V2, that is, the hare is strictlyfaster.
The hare still wants to be a bit lazy, so it decides to give the tortoise a headstart — the hare will wait for
an integer number of seconds before starting to run.
Unfortunately, the animals' measuring devices aren't up to par — they can only measure in integer
seconds, and will round up — so for example:
• Ifthe hare takes 1.57 seconds to finish, the reported time will be 2 seconds.
• Ifthe hare takes 3 seconds to finish, the reported time will be 3 seconds.
• Ifthe hare takes 3.01 seconds to finish. the reported time will be 4 seconds.
What's the longest time the hare can wait, while still being able to win the race?
Note that to win the race, the hare's reported time must be strictly less than the tortoise's.
Ifthe hare cannot win no matter what, print —1.
"""

from math import ceil

for _ in range(int(input())):
    track_length, v_tortoise, v_hare = map(int, input().split())

    print(ceil(track_length / v_tortoise) - ceil(track_length / v_hare) - 1)
