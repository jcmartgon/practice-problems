# Jesus Carlos Martinez Gonzalez
# 12/10/2023
# Janmansh and assignments (https://www.codechef.com/problems/JASSIGNMENTS)

"""
Janmansh has to submit 3 assignments for Chingari before 10 pm and he starts to do the assignments
at X pm. Each assignment takes him I hour to complete. Can you tell whether he'll be able to complete
all assignments on time or not?
Input Format
• The first line will contain T - the number oftest cases. Then the test cases follow.
• The first and only line of each test case contains one integer X - the time when Janmansh starts
doing the assignemnts.
"""

for _ in range(int(input())):
    print("Yes" if int(input()) <= 7 else "No")
