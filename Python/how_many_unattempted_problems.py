# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# How many unattempted problems (https://www.codechef.com/problems/PRACLIST)

"""
CodeChef recently revamped its practice page to make it easier for users to identify the next problems
they should solve by introducing some new features:
• Recent Contest Problems - contains only problems from the last 2 contests
• Separate Un-Attempted, Attempted, and All tabs
• Problem Difficulty Rating- the Recommended dropdown menu has various difficulty ranges so that
you can attempt the problems most suited to your experience
• Popular Topics and Tags
Our Chef is currently practicing on CodeChef and is a beginner. The count of 'All Problems' in the
Beginner section is X. Our Chef has already 'Attempted' Y problems among them. How many
roblems are et'lJn-attem ted?
"""

x, y = map(int, input().split())
print(x - y)
