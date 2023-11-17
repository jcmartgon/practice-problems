# Jesus Carlos Martinez Gonzalez
# 16/11/2023
# Single-use attack (https://www.codechef.com/problems/SINGLEUSE)

"""
Chef is playing a video game, and is now fighting the final boss.
The boss has H health points. Each attack of Chef reduces the health of the boss by X.
Chef also has a special attack that can be used at most once, and will decrease the health of the boss
Chef wins when the health of the boss is < 0.
What is the minimum number of attacks needed by Chef to win?
"""


from math import ceil

for _ in range(int(input())):
    boss_hp, common_hit, special_hit = map(int, input().split())
    print(1 + ceil((boss_hp - special_hit) / common_hit))
