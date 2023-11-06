# Jesus Carlos Martinez Gonzalez
# 06/09/2023
# Chef and water bottles (https://www.codechef.com/problems/CHEFBOTTLE)

"""
Chef has N empty bottles where each bottle has a capacity of X litres.
There is a water tank in Chefland having K litres of water. Chef wants to fill the empty bottles using the
water in the tank.
Assuming that Chef does not spill any water while filling the bottles, find out the maximum number of
bottles Chef can fill completely.
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(min(c // b, a))
