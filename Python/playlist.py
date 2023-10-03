# Jesus Carlos Martinez Gonzalez
# 02/10/2023
# Playlist (https://www.codechef.com/problems/SONGS)

"""
Chefs playlist contains 3 songs named A, B. and C each of duration exactly X minutes. Chef
generally plays these 3 songs in loop, i.e, A B —+ C A —+ B —+ C —+ A ...
Chef went on a train journey of N minutes and played his playlist on loop for the whole journey. How
many times did he listen to the song C completely?
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a // (3 * b))
