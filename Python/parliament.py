# Jesus Carlos Martinez Gonzalez
# 30/08/2023
# Parliament (https://www.codechef.com/problems/PARLIAMENT)

"""
An important resolution is being discussed in the Parliament of Chefland. There are N members
present in the Parliament out of which X members voted in favour of the resolution and the remaining
voted against it.
According to the constitution of Chefland, a resolution is passed if and only if half or more than half the
members present in the Parliament vote in favour of the resolution.
Determine if the resolution is passed or not.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if b >= a / 2 else "NO")
