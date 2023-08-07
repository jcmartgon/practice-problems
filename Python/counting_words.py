# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Counting words (https://www.codechef.com/problems/CNTWRD)

"""
Harsh was recently gifted a book consisting of N pages. Each page contains exactly M words printed
n it. As he was bored, he decided to count the number of words in the book.
Help Harsh find the total number of words in the book.
"""

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(x * y)
