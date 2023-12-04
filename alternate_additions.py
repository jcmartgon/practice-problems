# Jesus Carlos Martinez Gonzalez
# 04/12/2023
# Alternate additions (https://www.codechef.com/problems/ALTERADD)

"""
Chef has 2 numbers A and B (A < B).
Chef will perform some operations on A.
In the i operation:
• Chef will add I to A ifiis odd.
• Chef will add 2 to A if iis even.
Chef can stop at any instant. Can Chef make A equal to B?
"""

for _ in range(int(input())):
    a, b = map(int, input().split())

    print("YES" if (b - a) % 3 != 2 else "NO")
