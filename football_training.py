# Jesus Carlos Martinez Gonzalez
# 12/04/2024
# Football training (https://www.codechef.com/problems/MESSI)

"""
As a football trainer, you have several players training under you. Each of these players are fans of
either Leo or Ronald but not both.
• X of the players are fans of Leo, and want a free kick session to be carried out.
Y of the players are fans of Ronald, and want a penalty session to be carried out.
Note that each player is a fan of exactly one of Leo or Ronald, so there are X + Y players in total.
It'd be nice if players are actually interested in their training. so you decide to hold whichever type of
training has more people interested in it.
Given X and Y, which type of training session will you hold?
It is guaranteed that X Y.
"""

messi, ronaldo = map(int, input().split())

print("FREEKICK" if messi > ronaldo else "PENALTY")
