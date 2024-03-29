# Jesus Carlos Martinez Gonzalez
# 13/12/2023
# Drunk alcoholic (https://www.codechef.com/problems/DRUNKALK)

"""
Faizal is very sad after finding out that he is responsible for Sardar's death. He tries to drown his
sorrows in alcohol and gets very drunk. Now he wants to return home but is unable to walk straight.
For every 3 steps forward, he ends up walking one step backward.
Formally, in the ISt second he moves 3 steps forward, in the 2nd second he moves 1 step backwards, in
the 3rd second he moves 3 steps forward, in 4th second I step backwards, and so on.
How far from his initial position will Faizal be after k seconds have passed? Assume that Faizal's initial
position is 0.
"""

from math import ceil

for _ in range(int(input())):
    n = int(input())

    q, r = divmod(n, 2)

    print((q + ceil(r)) * 3 - q)
