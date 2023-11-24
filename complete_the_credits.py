# Jesus Carlos Martinez Gonzalez
# 23/11/2023
# Complete the credits (https://www.codechef.com/problems/CREDITS)

"""
In Uttu's college, a semester is said to be a:
• Overload semester if the number of credits taken > 65.
• Underload semester if the number of credits taken < 35.
• Normal semester otherwise
Given the number of credits X taken by Uttu, determine whether the semester is overload, Underload
or Normal.
"""


for _ in range(int(input())):
    credits = int(input())

    print("Overload" if credits > 65 else "Normal" if credits >= 35 else "Underload")
