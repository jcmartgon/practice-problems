# Jesus Carlos Martinez Gonzalez
# 03/09/2023
# Watching movies at 2x (https://www.codechef.com/problems/MOVIE2X)

"""
Chef started watching a movie that runs for a total of X minutes.
Chef has decided to watch the first Y minutes of the movie at twice the usual speed as he was warned
by his friends that the movie gets interesting only after the first Y minutes.
How long will Chef spend watching the movie in total?
Note: It is guaranteed that Y is even.
"""

a, b = map(int, input().split())
print(int(a - b * 0.5))
