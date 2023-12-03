# Jesus Carlos Martinez Gonzalez
# 03/12/2023
# Area or perimeter (https://www.codechef.com/problems/AREAPERI)

"""
Write a program to obtain length (L) and breadth (B) of a rectangle and check whether its area is
greater or perimeter is greater or both are equal.
"""

length = int(input())
breadth = int(input())

perimeter = length * 2 + breadth * 2
area = length * breadth

print(
    "Peri" if perimeter > area else "Area" if area > perimeter else "Eq",
    max(perimeter, area),
    sep="\n",
)
