# Jesus Carlos Martinez Gonzalez
# 19/12/2023
# Utkarsh and placement tests (https://www.codechef.com/problems/UTKPLC)

"""
Utkarsh is currently sitting for placements. He has applied to three companies named A, B, and C
You know Utkarsh'S order of preference among these 3 companies, given to you as characters first,
second, and third respectively (where first is the company he prefers most).
You also know that Utkarsh has received offers from exactly two of these three companies, given you
as characters and y.
Utkarsh will always accept the offer from whichever company is highest on his preference list. Which
company will he join?
"""

for _ in range(int(input())):
    preferences = input().split()
    offers = input().split()

    for preference in preferences:
        if preference in offers:
            print(preference)
            break
