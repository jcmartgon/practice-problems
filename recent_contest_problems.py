# Jesus Carlos Martinez Gonzalez
# 20/11/2023
# Recent contest problems (https://www.codechef.com/problems/RECENTCONT)

"""
CodeChef recently revamped its practice page to make it easier for users to identify the next problems
they should solve by introducing some new features:
• Recent Contest Problems - Contains only problems from the last 2 contests
• Separate Un-Attempted, Attempted and All tabs
• Problem Difficulty Rating- The Recommended dropdown menu has various difficultyranges so that
you can attempt the problems most suited to your experience
• Popular Topics and Tags
Chef has been participating regularly in rated contests but missed the last two contests due to his
college exams. He now wants to solve them and so he visits the practice page to view these problems.
Given a list of N contest codes, where each contest code is either START38 or L TIME1e8, help Chef
count how many problems were featured in each of the contests.
"""


for _ in range(int(input())):
    n = int(input())
    problems = [x for x in input().split()]

    print(problems.count("START38"), problems.count("LTIME108"))
