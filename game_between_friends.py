# Jesus Carlos Martinez Gonzalez
# 19/03/2024
# Game between friends (https://www.codechef.com/problems/FRGAME)

"""
Nitin and Sobhagya were playing a game with coins. If Sobhagya has more coins then he is winning
otherwise Nitin is winning. Note that this means if both Nitin and Sobhagya have the same number of
coins, then Nitin is winning.
Initially Nitin has A coins while Sobhagya has B coins. Then Ritik came and gave his C coins to the
player who is not winning currently, after which Satyarth came and repeated the same process (gave
his D coins to the player who is not winning currently).
Find the final winner of the game.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    if a < b:
        a += c
    else:
        b += c

    if a < b:
        a += d
    else:
        b += d

    print("S" if a < b else "N")
