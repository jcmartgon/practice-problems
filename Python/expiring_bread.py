# Jesus Carlos Martinez Gonzalez
# 07/09/2023
# Expiring bread (https://www.codechef.com/problems/EXPIRY)

"""
Eikooc loves bread. She has N loaves of bread, all of which expire after exactly M days. She can eat
upto K loaves of bread in a day. Can she eat all the loaves of bread before they expire?
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if b * c >= a else "NO")
