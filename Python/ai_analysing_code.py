# Jesus Carlos Martinez Gonzalez
# 08/09/2023
# AI Analysing Code (https://www.codechef.com/problems/AIANALYSE)

"""
Chefhas recently introduced a feature which allows you to open any users submitted code (notjust
your own); and ask an Al to explain that code in English. For example, you can go to
https://nww.codechef.com/viewsolution/70530506 and click on "Analyse This Code".
But there is a restriction that the feature works only on codes which are at most 1000 characters long.
Given the number of characters, C, in a particular code, output whether the feature is available on this
code or not.
"""

print("YES" if int(input()) <= 1000 else "NO")
