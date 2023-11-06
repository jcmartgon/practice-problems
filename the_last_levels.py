# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# The last levels (https://www.codechef.com/problems/LASTLEVELS)

"""
Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of the game in
a single session.
There are X levels remaining in the game, and each level takes Chef Y minutes to complete. To
protect against eye strain, Chef also decides that every time he completes 3 levels. he will take a Z
minute break from playing. Note that there is no need to take this break if the game has been
completed.
How much time (in minutes) will it take Chef to complete the game?
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    base = a * b
    q, r = divmod(a, 3)
    breaks = (q - 1) * c if r == 0 else q * c
    print(base + breaks)
