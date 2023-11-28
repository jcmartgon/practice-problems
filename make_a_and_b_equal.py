# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Make a and b equal (https://www.codechef.com/problems/EQUALISE)

"""
Chef has two numbers A and B.
In one operation, Chef can choose either A or B and multiply it by 2.
Determine whether he can make both A and B equal after any number (possibly, zero) of moves.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())

    c = min(a, b)

    while c < max(a, b):
        c *= 2

    print("YES" if c == max(a, b) else "NO")
