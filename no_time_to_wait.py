# Jesus Carlos Martinez Gonzalez
# 05/03/2024
# No time to wait (https://www.codechef.com/problems/NOTIME)

"""
Only x hours are left for the March Long Challenge and Chef is only left with the last problem unsolved.
However, he is sure that he cannot solve the problem in the remaining time. From experience, he
figures out that he needs exactly H hours to solve the problem.
Now Chef finally decides to use his special power which he has gained through years of intense yoga.
He can travel back in time when he concentrates. Specifically, his power allows him to travel to N
different time zones, which are Tl, T2, ... , TN hours respectively behind his current time.
Find out whether Chef can use one of the available time zones to solve the problem and submit it
before the contest ends.
"""

n, time_needed, time_left = map(int, input().split())
time_zones = [int(x) for x in input().split()]
flag = False

for time_zone in time_zones:
    if time_left + time_zone >= time_needed:
        flag = True
        break

print("YES" if flag else "NO")
