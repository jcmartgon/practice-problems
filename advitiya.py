# Jesus Carlos Martinez Gonzalez
# 26/03/2024
# Summer time (https://www.codechef.com/problems/MANGOLASSI)

"""
IIT Ropar is hosting its tech fest, Advitiya. on the 16-th, 17-th, and 18-th of February.
Mehul, looking for a vacation, decides to visit Ropar in the month of February.
Mehul learned of Advitiya, and found out that there are no registration fees — even accommodation is
being provided to the participants for free!
Team Advitiya is very welcoming, so Mehul definitely wants to attend the fest.
Mehul will visit Ropar on date N (which is between 1 and 18) of February. Will he be able to enjoy the
fest?
Print "ADVITIYA" if N is one of the days on which Advitiya is running, and "WAITING FOR ADVITIYA"
otherwise.
"""

print("Advitiya" if input() in ["16", "17", "18"] else "WAITING FOR ADVITIYA")
