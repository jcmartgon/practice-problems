# Jesus Carlos Martinez Gonzalez
# 29/10/2023
# Monopoly (https://www.codechef.com/problems/MONOPOLY2)

"""
There are 4 companies in the markets of Chefland, A, B, C, and D.
This year,
• Company A made a profit of P lakh rupees,
• Company B made a profit of Q lakh rupees,
• Company C made a profit of R lakh rupees,
• Company D made a profit of S lakh rupees.
There is said to be a monopoly in the market if the profit made by one company is strictly greater
than the sum of profits made by all other companies.
Determine if there is a monopoly in the market or not.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(
        "YES"
        if a > b + c + d or b > a + c + d or c > a + b + d or d > a + b + c
        else "NO"
    )
