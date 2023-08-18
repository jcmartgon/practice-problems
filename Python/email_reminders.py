# Jesus Carlos Martinez Gonzalez
# 17/08/2023
# Email reminders (https://www.codechef.com/problems/EMAILREM)

"""
MoEngage helps the Chef send email reminders about rated contests to the participants.
There are a total of N participants on Chefs platform, and U of them have told Chef not to send
emails to them.
If so, how many participants should MoEngage send the contest emails to?
"""

a, b = map(int, input().split())
print(a - b)
