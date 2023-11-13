# Jesus Carlos Martinez Gonzalez
# 12/11/2023
# Valid triangles (https://www.codechef.com/problems/FLOW013)

"""
Write a program to check whether a triangle is valid or not, when the three angles of the triangle are
the inputs. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a + b + c == 180 else "NO")
