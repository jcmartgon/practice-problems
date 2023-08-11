# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Read pages (https://www.codechef.com/problems/READPAGES)

"""
Chef has started studying for the upcoming test. The textbook has N pages in total. Chef wants to read
at most X pages a day for Y days.
Find out whether it is possible for Chef to complete the whole book.
"""

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print("YES" if y * z >= x else "NO")
