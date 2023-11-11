# Jesus Carlos Martinez Gonzalez
# 10/11/2023
# Pass or fail (https://www.codechef.com/problems/PASSORFAIL)

"""
Chef is struggling to pass a certain college course.
The test has a total of N questions. each question carries 3 marks for a correct answer and —1 for an
incorrect answer. Chef is a risk-averse person so he decided to attempt all the questions. It is known
that Chef got X questions correct and the rest of them incorrect. For Chef to pass the course he must
score at least P marks.
Will Chef be able to pass the exam or not?
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("PASS" if b * 3 - (a - b) >= c else "FAIL")
