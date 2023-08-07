# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# My very 1st contest (https://www.codechef.com/problems/MY1STCONTEST)

"""
Each contest - there are approximately 1500 - 2000 users who participate for the 1st time and get
rated.
The Chef wanted to tel/ new users some tricks for their 1st contest:
• Before the contest-you donthaveanyrating. So even if you make a single submission -you will
become part of the contest rank list and you will get a rating.
• If you want your rating to increase-give the entire 2 hours to the contest & dontquit!/fyou keep
trying till the end, and the more time you get, the more problems you can solve. That means larger
rating increases!
• Do notaskyour friends for their code. If you copy paste their code, you will get caught during
plagiarism checks and your rating will be reduced by 275 points, along with a permanent black mark
on your profile.
Now to the problem:
In a contest where N new users visited the contest,
A users just saw the problems and didnt make any submissions and hence won't get any rating.
• B users who made a submission but could not solve any problem correctly. Thus, after the contest,
they will get a rating in the range 800 — 1000.
• Everyone else could correctly solve at least 1 problem. Thus, they will get a rating strictly greater
than 1000 after the contest.
You need to output the number of new users in the contest who, after the contest. will get a rating and
also the number of new users who will get a rating strictly greater than 1000.
"""

a, b, c = map(int, input().split())
print(a - b, a - b - c, end=" ")
