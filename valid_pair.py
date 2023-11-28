# Jesus Carlos Martinez Gonzalez
# 28/11/2023
# Valid pair (https://www.codechef.com/problems/SOCKS1)

"""
Chef has three socks in his drawer. Each sock has one of 10 possible colours, which are represented by
integers between I and IO. Specifically, the colours of the socks are A, B, and C.
Chef has to wear two socks which have the same colour. Help Chef find out if that is possible or not.
"""

a, b, c = input().split()

print("YES" if a == b or a == c or b == c else "NO")
