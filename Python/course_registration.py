# Jesus Carlos Martinez Gonzalez
# 19/09/2023
# Course registration (https://www.codechef.com/problems/COURSEREG)

"""
There is a group of N friends who wish to enroll in a course together. The course has a maximum
capacity of M students that can register for it. If there are K other students who have already enrolled
in the course, determine if it will still be possible for all the N friends to do so or not.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a + c <= b else "NO")
