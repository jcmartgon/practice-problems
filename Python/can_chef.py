# Jesus Carlos Martinez Gonzalez
# 20/09/2023
# Can chef (https://www.codechef.com/problems/CANCHEF)

"""
Chef owns a car that can run 15 kilometers using I liter of petrol.
He wants to attend a programming camp at DAIICT.
X liters of petrol is present in Chefs car. The distance between his house and DAIICT is Y kilometers.
Determine whether Chef can attend the event and return to his home with the given amount of petrol.
Note: Chef has to return back to home, so the total distance to be covered would be 2 • Y.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if a * 15 >= b * 2 else "NO")
