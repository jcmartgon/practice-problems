# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Chef on date (https://www.codechef.com/problems/CHEFONDATE)

"""
Chef and his girlfriend go on a date. Chef took X dollars with him, and was quite sure that this would
be enough to pay the bill. At the end, the waiter brought a bill of Y dollars. Print "YES" if Chef has
enough money to pay the bill, or "NO" if he has to borrow from his girlfriend and leave a bad
impression on her.
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print("YES" if x >= y else "NO")
