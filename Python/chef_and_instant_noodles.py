# Jesus Carlos Martinez Gonzalez
# 13/09/2023
# Chef and instant noodles (https://www.codechef.com/problems/INSTNOODLE)

"""
Chef has invented I-minute Instant Noodles. As the name suggests, each packet takes exactly I minute
to cook.
Chef's restaurant has X stoves and only 1 packet can be cooked in a single stove at any minute.
How many customers can Chef serve in Y minutes if each customer orders exactly 1 packet of
noodles?
"""

a, b = map(int, input().split())
print(a * b)
