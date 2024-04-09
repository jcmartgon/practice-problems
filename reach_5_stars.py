# Jesus Carlos Martinez Gonzalez
# 08/04/2024
# Reach 5 stars (https://www.codechef.com/problems/R5S)

"""
Chef loves giving contests on Codechef. Chef wants to become 5 star rated. Currently his rating on
Codechef is X.
After todays contest, his rating will increase by Y. Note that Y can be negative which means that
Chefs rating will decrease.
Find whether Chef will become 5 star rated after today's contest.
Chef will be considered 5 star rated if his rating is greater than or equal to 2000.
"""

initial, change = map(int, input().split())


print("YES" if initial + change >= 2000 else "NO")
