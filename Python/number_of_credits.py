# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Number of credits (https://www.codechef.com/problems/CREDS)

"""
In the current semester. you have taken X RTP courses. Y Audit courses and Z Non-RTP courses.
The credit distribution for the courses are:
• 4 credits for clearing each RTP course.
• 2 credits for clearing each Audit course.
• No credits for clearing a Non-RTP course.
Assuming that you cleared all your courses, report the number of credits you obtain this semester.
"""

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print(x * 4 + y * 2)
