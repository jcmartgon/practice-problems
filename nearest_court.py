# Jesus Carlos Martinez Gonzalez
# 24/11/2023
# Nearest court (https://www.codechef.com/problems/NEARESTCOURT)

"""
Chef and Chefina are at positions X and Y on a number line.
They both love badminton.
It is known that badminton courts are located at every integer point.
They want to find a court such that the maximum distance travelled by either of them is minimized.
Formally. suppose they choose the badminton court at position Z. You need to find the minimum value
of max(lX — ZI, I Y — ZI) across all possible choices of Z. Here, IXI denotes absolute value of X.
Report this minimum value.
"""


for _ in range(int(input())):
    x, y = map(int, input().split())

    z = (x + y) // 2
    print(max(x, y) - z)
