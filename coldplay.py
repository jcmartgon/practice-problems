# Jesus Carlos Martinez Gonzalez
# 02/12/2023
# Coldplay (https://www.codechef.com/problems/SLOOP)

"""
Chef is a big fan of Coldplay. Every Sunday, he will drive to a park taking M minutes to reach there, and
during the ride he will play a single song on a loop. Today, he has got the latest song which is in total S
minutes long. He is interested to know how many times will he be able to play the song completely.
"""

for _ in range(int(input())):
    trip, song = map(int, input().split())
    print(trip // song)
