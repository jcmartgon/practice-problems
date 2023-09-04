# Jesus Carlos Martinez Gonzalez
# 03/09/2023
# Scalene triangle (https://www.codechef.com/problems/SCALENE)

"""
Given A, B, and C as the sides of a triangle. find whether the triangle is scalene.
Note:
• A triangle is said to be scaleneif all three sides of the triangle are distinct.
• It is guaranteed that the sides represent a valid triangle.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a != b and a != c and b != c else "NO")
