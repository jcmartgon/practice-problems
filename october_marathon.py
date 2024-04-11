# Jesus Carlos Martinez Gonzalez
# 10/04/2024
# October marathon (https://www.codechef.com/problems/OCTATHON)

"""
Chef organised a 30 kilometres marathon in Chefland.
The participants receive medals on completing the marathon as following:
• If the total time taken is less than 3 hours, they receive a GOLD medal.
• Ifthe total time taken is greater than equal to 3 hours but less than 6 hours, they receive a SILVER
medal.
• Ifthe total time taken is greater than equal to 6 hours, they receive a BRONZE medal.
Chefina participated in the marathon and completed it in X hours. Which medal would she receive?
"""

time = int(input())

print("GOLD" if time < 3 else "SILVER" if time < 6 else "BRONZE")
