# Jesus Carlos Martinez Gonzalez
# 25/11/2023
# Equalizing numbers (https://www.codechef.com/problems/EQLZING)

"""
Chef has two integers A and B. In one operation he can choose any integer d, and make one of the
following two moves :
• Add dto A and subtract dfrom B.
Add dto B and subtract dfrom A.
Chef is allowed to make as many operations as he wants. Can he make A and B equal?
"""


for _ in range(int(input())):
    a, b = map(int, input().split())

    print("YES" if abs(a - b) % 2 == 0 else "NO")
