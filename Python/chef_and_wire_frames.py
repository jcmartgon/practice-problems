# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# Chef and wire frames (https://www.codechef.com/problems/CWIREFRAME)

"""
Chef has a rectangular plate of length Ncm and width Mcm. He wants to make a wireframe around
the plate. The wireframe costs X rupees per cm.
Determine the cost Chef needs to incur to buy the wireframe.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print((2 * a + 2 * b) * c)
