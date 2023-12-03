# Jesus Carlos Martinez Gonzalez
# 03/12/2023
# Chefland visa (https://www.codechef.com/problems/VISA)

"""
Ash is trying to get visa to Chefland. For the visa to be approved. he needs to satisfy the following three
criteria:
• Solve at least problems on Codechef.
• Have at least YI current rating on Codechef.
• Make his last submission at most ZI months ago.
You are given the number of problems solved by Chef (0), his current rating (u) and the information
that he made his last submission z.2 months ago. Determine whether he will get the visa.
"""

for _ in range(int(input())):
    (
        problems_required,
        problems_current,
        rating_required,
        rating_current,
        activity_required,
        activity_current,
    ) = map(int, input().split())

    print(
        "YES"
        if problems_current >= problems_required
        and rating_current >= rating_required
        and activity_current <= activity_required
        else "NO"
    )
