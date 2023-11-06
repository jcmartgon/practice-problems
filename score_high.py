# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Score high (https://www.codechef.com/problems/HIGHSCORE)

"""
Chef is taking a tough examination. The question paper consists of N objective problems and each
problem has 4 options A, B, C, and D, out of which, exactly one option is correct.
Since Chef did not study for the exam, he does not know the answer to any of the problems. Chef was
looking nearby for help when his friend somehow communicated the following information:
• Exactly NA problems have option A as the answer.
• Exactly NB problems have option B as the answer.
• Exactly Nc problems have option C as the answer.
• Exactly ND problems have option D as the answer.
Note that:
• Each problem is worth exactly 1 mark and there is no negative marking.
• Even though Chef knows the number of correct options of each type, he does not know the correct
answer to any problem.
Based on the given information, find the maximum marks Chef can guarantee if he marks the
answers optimally.
"""

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    print(max(lst))
