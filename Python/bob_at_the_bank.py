# Jesus Carlos Martinez Gonzalez
# 26/09/2023
# Bob at the bank (https://www.codechef.com/problems/BOBBANK)

"""
Bob has an account in the Bobby Bank. His current account balance is W rupees.
Each month, the office in which Bob works deposits a fixed amount of X rupees to his account.
Y rupees is deducted from Bob's account each month as bank charges.
Find his final account balance after Z months. Note that the account balance can be negative as well.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(a + (b - c) * d)
