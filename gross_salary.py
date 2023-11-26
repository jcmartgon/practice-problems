# Jesus Carlos Martinez Gonzalez
# 25/11/2023
# Gross salary (https://www.codechef.com/problems/FLOW011)

"""
In a company an emplopyee is paid as under: If his basic salary is less than Rs. 1500, then HRA = 10% of
base salary and DA = 90% of basic salary.
If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the
Employee's salary is input. write a program to find his gross salary.
NOTE: Gross salary = Basic salary + HRA + DA
"""


for _ in range(int(input())):
    salary = int(input())

    print(salary * 2 if salary < 1500 else salary + 500 + salary * 0.98)
