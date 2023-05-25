# Jesus Carlos Martinez Gonzalez
# 25/05/23
# Nested Lists (https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true)

"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

if __name__ == "__main__":
    students = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, float(score)])

        scores.append(float(score))

scores = list(set(scores))
scores.sort()

score = scores[1]

students = sorted(students, key=lambda v: (v[1], v[0]))

for student in students:
    if student[1] == score:
        print(student[0])
