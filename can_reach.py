# Jesus Carlos Martinez Gonzalez
# 20/03/2024
# Can reach (https://www.codechef.com/problems/CAN_REACH)

"""
A first-year student, came to your college. Being a good senior, you must tell him if it is possible to go
from College Main Gate to Hostel for him.
The college can be visualized on a 2D-pIane. Suppose the College Main Gate is situated at origin i.e. at
the coordinates (0, 0) and the Hostel is situated at the coordinates (x, y).
As the first-year student wants to explore the college campus further, in one move, he will increase or
decrease any coordinate (either the x-coordinate or the y-coordinate) by a value of exactly K.
Is it possible for the first-year student to reach the Hostel?
"""

for _ in range(int(input())):
    x, y, steps = map(int, input().split())

    print("YES" if x % steps == 0 and y % steps == 0 else "NO")
