# Jesus Carlos Martinez Gonzalez
# 14/12/2023
# Chef on island (https://www.codechef.com/problems/CCISLAND)

"""
Suppose Chef is stuck on an island and currently he has units of food supply and y units of water
supply in total that he could collect from the island. He needs units of food supply and yr units of
water supply per day at the minimal to have sufficient energy to build a boat from the woods and also
to live for another day. Assuming it takes exactly D days to build the boat and reach the shore, tell
whether Chef has the sufficient amount of supplies to be able to reach the shore by building the boat?
"""

for _ in range(int(input())):
    food_total, water_total, food_req, water_req, days = map(int, input().split())

    print(
        "YES"
        if food_total >= food_req * days and water_total >= water_req * days
        else "NO"
    )
