# Jesus Carlos Martinez Gonzalez
# 18/08/2023
# Rating improvement (https://www.codechef.com/problems/ADVANCE)

"""
Chefs current rating is X, and he wants to improve it. It is generally recommended that a person with
rating X should solve problems whose difficulty lies in the range [X, X + 2001, i.e. problems whose
difficulty is at least X and at most X + 200.
You find out that Chef is currently solving problems with a difficulty of Y.
Is Chef following the recommended practice or not?
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print("YES" if x <= y <= x + 200 else "NO")
