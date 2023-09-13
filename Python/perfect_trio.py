# Jesus Carlos Martinez Gonzalez
# 12/09/2023
# Perfect Trio (https://www.codechef.com/problems/PERFECTTRIO)

"""
Chef defines a group of three friends as a perfect group if the age of one person is equal to the sum of
the age of remaining two people.
Given that. the ages of three people in a group are A, B, and C respectively, find whether the group is
perfect
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a + b == c or a + c == b or b + c == a else "NO")
