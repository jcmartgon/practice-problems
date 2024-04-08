# Jesus Carlos Martinez Gonzalez
# 07/04/2024
# Bone appetit (https://www.codechef.com/problems/BNE_APT)

"""
Trick or treat, bags of sweets, ghosts are walking down the street
It's Halloween and Suri Bhai is out to get his treats.
There are two sectors in his neighborhood, "Bones" and "Blood". They have N and M people,
respectively.
Each person in "Bones" will hand out X treats, and each person in "Blood" will hand out Y treats.
How many treats does Suri Bhai get from visiting everyone in his neighborhood in total?
"""

bones_people, blood_people = map(int, input().split())
bones_treats, blood_treats = map(int, input().split())

print(bones_people * bones_treats + blood_people * blood_treats)
