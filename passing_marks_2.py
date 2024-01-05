# Jesus Carlos Martinez Gonzalez
# 04/01/2024
# Passing marks (https://www.codechef.com/problems/PSGRADE)

"""
Recently, Chefs College Examination has concluded. He was enrolled in 3 courses and he scored
A, B, Cin them, respectively. To pass the semester, he must score at least A - , B • , Cmin marks in
the respective subjects along with a cumulative score of at least T • i.e. A + B + C > T
Given seven integers Amin, min, min, ,
B C T A B, C tell whether Chef passes the semester or not.
"""

for _ in range(int(input())):
    a_min, b_min, c_min, t_min, a, b, c = map(int, input().split())

    print(
        "YES"
        if a >= a_min and b >= b_min and c >= c_min and a + b + c >= t_min
        else "NO"
    )
