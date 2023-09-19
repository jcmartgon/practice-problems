# Jesus Carlos Martinez Gonzalez
# 18/09/2023
# Practice makes us perfect (https://www.codechef.com/problems/PRACTICEPERF)

"""
Most programmers will tell you that one of the ways to improve your performance in competitive
programming is to practice a lot of problems.
Our Chef took the above advice very seriously and decided to set a target for himself.
• Chef decides to solve at least 10 problems every week for 4 weeks.
Given the number of problems he actually solved in each week over 4 weeks as Pl, P2, Pg, and P4,
output the number of weeks in which Chef met his target.
"""

weeks = map(int, input().split())
x = 0
for problems in weeks:
    if problems >= 10:
        x += 1
print(x)
