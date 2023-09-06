# Jesus Carlos Martinez Gonzalez
# 05/09/2023
# Speciality (https://www.codechef.com/problems/SPECIALITY)

"""
On every CodeChef user's profile page, the list of problems that they have set, tested. and written
editorials for, is listed at the bottom.
Given the number of problems in each of these 3 categories as X, Y, and Z respectively (where all
three integers are distinct), find if the user has been most active as a setter, Tester. or
Editorialist.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a > b and a > c:
        print("Setter")
    elif b > c and b > a:
        print("Tester")
    else:
        print("Editorialist")
