# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Finding square roots (https://www.codechef.com/problems/FSQRT)

"""
In olden days finding square roots seemed to be difficult but nowadays it can be easily done using in-
built functions available across many languages.
Assume that you happen to hear the above words and you want to give a try in finding the square root
of any given integer using in-built functions. So here's your chance.
"""

# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

# Note that it's python3 Code. Here, we are using input() instead of raw_input().
# You can check on your local machine the version of python by typing "python --version" in the terminal.

import math

t = int(input())
for i in range(t):
    n = int(input())
    print(int(math.sqrt(n)))
