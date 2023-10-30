# Jesus Carlos Martinez Gonzalez
# 30/10/2023
# High accuracy (https://www.codechef.com/problems/ACCURACY)

"""
There are 100 questions in a paper. Each question carries +3 marks for correct answer, -1 marks for
incorrect answer and e marks for unattempted question.
It is given that Chef received exactly X (0 < X < 100) marks. Determine the minimum number of
problems Chef marked incorrect.
"""

from math import ceil, floor

for _ in range(int(input())):
    x = int(input())
    n = x / 3
    print(3 * (ceil(n)) - floor(x))
