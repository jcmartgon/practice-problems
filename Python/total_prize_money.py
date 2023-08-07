# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Total prize money (https://www.codechef.com/problems/PRIZEPOOL)

"""
In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:
• Top 10 participants receive rupees X each.
• Participants with rank 11 to 100 (both inclusive) receive rupees Y each.
Find the total prize money over all the contestants.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(10 * x + 90 * y)
