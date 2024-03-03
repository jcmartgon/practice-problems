# Jesus Carlos Martinez Gonzalez
# 02/03/2024
# Difficulty rating order (https://www.codechef.com/problems/RATINGINPRAC)

"""
Our Chef has some students in his coding class who are practicing problems. Given the difficulty of the
problems that the students have solved in order, help the Chef identify if they are solving them in non-
decreasing order of difficulty. Non-decreasing means that the values in an array is either increasing or
remaining the same. but not decreasing. That is. the students should not solve a problem with difficulty
dl, and then later a problem with difficulty 4, where dl > 4.
Output "Yes" if the problems are attempted in non-decreasing order of difficulty rating and "No" if not.
"""

t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))

    tmp = d[0]
    flag = True

    for problem in d[1:]:
        if problem < tmp:
            flag = False
            break
        tmp = problem

    print("Yes" if flag else "No")

    t -= 1
