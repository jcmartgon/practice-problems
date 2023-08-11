# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Chef requirement (https://www.codechef.com/problems/CHAIRS_)

"""
Chefs coding class is very famous in Chefland.
This year X students joined his class and each student will require one chair to sit on. Chef already has
Y chairs in his class. Determine the minimum number of new chairs Chef must buy so that every
student is able to get one chair to sit on.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x - y if x > y else 0)
