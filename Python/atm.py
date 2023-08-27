# Jesus Carlos Martinez Gonzalez
# 26/08/2023
# ATM (https://www.codechef.com/problems/HS08TEST)

"""
Pooja would like to withdraw X SUS from an ATM. The cash machine will only accept the transaction if X
is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction
(including bank charges). For each successful withdrawal the bank charges 0.50 SIJS.
Calculate Pooja's account balance after an attempted transaction.
"""

# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

# Note that it's python3 Code. Here, we are using input() instead of raw_input().
# You can check on your local machine the version of python by typing "python --version" in the terminal.

n, atm = map(float, input().split())
n = int(n)
if n + 0.5 <= atm and n % 5 == 0:
    print(float(atm - n - 0.5))
else:
    print(float(atm))
