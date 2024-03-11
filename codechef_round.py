# Jesus Carlos Martinez Gonzalez
# 10/03/2024
# Codechef round (https://www.codechef.com/problems/CODECHEF)

"""
Codechef rounds are held on every Wednesday now, and not on any other days.
You are wondering whether there is a Codechef round today. You know it is the Nth day of the week
(Sunday is 1st, Monday is 2nd, Tuesday is 3rd, Wednesday is 4th and so on).
Can you tell whether there is a Codechef round today?
"""

print("YES" if int(input()) % 7 == 4 else "NO")
