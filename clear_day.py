# Jesus Carlos Martinez Gonzalez
# 14/03/2024
# Clear day (https://www.codechef.com/problems/CLEARDAY)

"""
Chef classifies a day to be either rainy, cloudy, or clear.
In a particular week. Chef finds X days to be rainy and Y days to be cloudy.
Find the number of clear days in the week.
"""

print(7 - sum([int(x) for x in input().split()]))
