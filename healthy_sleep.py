# Jesus Carlos Martinez Gonzalez
# 28/03/2024
# Healthy sleep (https://www.codechef.com/problems/HEALSE)

"""
At 111TA, students have diverse sleep patterns, and there isn't a fixed duration for their daily sleep.
Typical scientific recommendations suggest that the duration of a healthy sleep is 8 hours per day.
As you begin your journey as a programmer, you've been tasked by the renowned programmer of
111TA, Pavitra Pandey, with your first project.
Your assignment is to write a program that takes as input the number of hours a student sleeps per
day, and judges how good their sleep schedule is. Specifically,
• Ifthe student sleeps for strictly less than 8 hours, the program should output LESS.
• Ifthe student sleeps for exactly8 hours. the program should output PERFECT.
• Ifthe student sleeps for strictly more than 8 hours. the program should output MORE.
Can you write such a program?
"""

sleep_hours = int(input())

print("LESS" if sleep_hours < 8 else "MORE" if sleep_hours > 8 else "PERFECT")
