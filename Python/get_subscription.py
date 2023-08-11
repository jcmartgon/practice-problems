# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Subscribe (https://www.codechef.com/problems/SUBSCRIBE)

"""
Chef wants to conduct a lecture for which he needs to set up an online meeting of exactly X minutes.
The meeting platform supports a meeting of maximum 30 minutes without subscription and a meeting
of unlimited duration with subscription.
Determine whether Chef needs to take a subscription or not for setting up the meet.
"""

for _ in range(int(input())):
    print("YES" if int(input()) > 30 else "NO")
