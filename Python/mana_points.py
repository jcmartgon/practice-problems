# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Mana points (https://www.codechef.com/problems/MANAPTS)

"""
Chef is playing a mobile game. In the game, Chef's character Chefario can perform special attacks.
However, one special attack costs X mana points to Chefario.
If Chefario currently has Y mana points, determine the maximum number of special attacks he can
perform.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y // x)
