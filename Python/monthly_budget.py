# Jesus Carlos Martinez Gonzalez
# 14/09/2023
# Monthly budget (https://www.codechef.com/problems/BUDGET_)

"""
Akshat has X rupees to spend in the current month. His daily expenditure is Y rupees. i.e., he spends
Y rupees each day.
Given that the current month has 30 days, find out if Akshat has enough money to meet his daily
expenditures for this month.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if a >= b * 30 else "NO")
