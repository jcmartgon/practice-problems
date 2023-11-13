# Jesus Carlos Martinez Gonzalez
# 12/11/2023
# Far from origin (https://www.codechef.com/problems/FARFROMO)

"""
Alex. Bob, and, Chef are standing on the coordinate plane. Chef is standing at the origin (coordinates
(O, O)) while the location of Alex and Bob are (Xl, YI) and (X2, Y2) respectively.
Amongst Alex and Bob, find out who is at a farther distance from Chef or determine if both are at the
same distance from Chef.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a + b + c == 180 else "NO")
