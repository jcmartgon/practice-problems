# Jesus Carlos Martinez Gonzalez
# 14/04/2024
# All new codechef (https://www.codechef.com/problems/NEWCC)

"""
CodeChef hasjust finished migcatLng to a newjudging system.
Chef would like to test the performance of the new judging system.
Chef has some code for an older task, which he knows ran in X milliseconds on the old judging server.
On resubmitting the code to the new judging server, it ran in Y milliseconds.
Which judging system is faster?
"""

old, new = map(int, input().split())

print("OLD" if old < new else "NEW" if old > new else "SAME")
