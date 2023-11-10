# Jesus Carlos Martinez Gonzalez
# 09/09/2023
# Too many floors (https://www.codechef.com/problems/FLOORS)

"""
Chef and Chefina are residing in a hotel.
There are IO floors in the hotel and each floor consists of IO rooms.

- Floor I consists of room numbers I to IO.
- Floor 2 consists of room numbers 11 to 20.
- Floor i consists of room numbers 10 • (i — 1) + 1 to 10 • i

You know that Chef's room number is X while Chefinars Room number is Y.
If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.
"""

from math import ceil

for _ in range(int(input())):
    a, b = map(lambda x: ceil(int(x) / 10), input().split())
    print(abs(a - b))
