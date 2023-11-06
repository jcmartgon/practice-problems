# Jesus Carlos Martinez Gonzalez
# 05/09/2023
# Mario and bullet (https://www.codechef.com/problems/BULLET)

"""
Mario's bullet moves at X pixels per frame. He wishes to shoot a goomba standing Y pixels away from him. The
goomba does not move.
Find the minimum time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after
at least Z seconds from now.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(max(c - b // a, 0))
