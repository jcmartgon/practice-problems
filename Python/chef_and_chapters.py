# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Chef and chapters (https://www.codechef.com/problems/SEMCOURSES)

"""
This semester, Chef took X courses. Each course has Y units and each unit has Z chapters in it.
Find the total number of chapters Chef has to study this semester.
"""

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print(x * y * z)
