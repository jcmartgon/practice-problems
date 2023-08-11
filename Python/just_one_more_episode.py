# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Just one more episode (https://www.codechef.com/problems/ONEMORE)

"""
Chef has to attend an exam that starts in X minutes, but of course, watching shows takes priority.
Every episode of the show that Chef is watching, is 24 minutes long.
If he starts watching a new episode now, will he finish watching it strictly before the exam starts?
"""

for _ in range(int(input())):
    x = int(input())
    print("YES" if x > 24 else "NO")
