# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Passes for fair (https://www.codechef.com/problems/FAIRPASS)

"""
There is a fair going on in Chefland. Chef wants to visit the fair along with his N friends. Chef manages
to collect K passes for the fair. Will Chef be able to enter the fair with all his N friends?
A person can enter the fair using one pass, and each pass can be used by only one person.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print("YES" if y > x else "NO")
