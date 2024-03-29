# Jesus Carlos Martinez Gonzalez
# 10/11/2023
# Expense list (https://www.codechef.com/problems/EXPENSES)

"""
Chef has made a list for his monthly expenses. The list has N expenses with index I to N. The money
spent on each expense depends upon the monthly income of Chef.
• Chef spends 50% of his total income on the expense with index 1.
• The money spent on the expense (i > I) is equal to 50% of the amount remaining after paying
for all expenses with indices less than i
Given that Chef earns 2x rupees in a month, find the amount he saves after paying for all N expenses.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(pow(2, b - a))
