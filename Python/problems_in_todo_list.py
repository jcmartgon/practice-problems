# Jesus Carlos Martinez Gonzalez
# 29/10/2023
# Problems in your to-do list (https://www.codechef.com/problems/TODOLIST)

"""
CodeChef recently revamped its practice page to make it easier for users to identify the next problems
they should solve by introducing some new features:
• Recent Contest Problems - contains only problems from the last 2 contests
• Separate Un-Attempted, Attempted, and AI/ tabs
• Problem Difficulty Rating- the Recommended dropdown menu has various difficulty ranges so that
you can attempt the problems most suited to your experience
• Popular Topics and Tags
Like most users, Chef didnt know that he could add problems to a personal to-do list by clicking on the
magic '+' symbol on the top-right of each problem page. But once he found out about it. he went crazy
and added loads of problems to his to-do list without looking at their difficulty rating.
Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than
1000. Given a list of difficulty ratings for problems in the Chefs to-do list, please help him identify how
many of those problems Chef should remove from his to-do list, so that he is only left with problems of
difficulty rating less than 1000.
"""

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    print(sum(1 for x in lst if x >= 1000))
