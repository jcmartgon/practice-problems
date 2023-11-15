# Jesus Carlos Martinez Gonzalez
# 15/11/2023
# Helping chef (https://www.codechef.com/problems/FLOW008)

"""
Write a program, which takes an integer N and if the number is less than 10 then display "Thanks for
helping Chef!" otherwise print "-1
"""


for _ in range(int(input())):
    print("Thanks for helping Chef!" if int(input()) < 10 else "-1")
