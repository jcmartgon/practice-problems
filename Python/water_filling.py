# Jesus Carlos Martinez Gonzalez
# 19/10/2023
# Water Filling (https://www.codechef.com/problems/WATERFILLING)

"""
Chef has three water bottles. At any point, if at least two of them are empty, she will fill them up. But if
at most one bottle is empty, she will wait. and not fill them up now.
You are given three integers - Bl, B2, and Bg.
If Bl = I, it means that the first bottle is full.
If Bl = O, it means that the first bottle is empty.
Similarly. B2 denotes whether the second bottle is full or empty, and Bg denotes it for the third bottle.
Output "Water filling time", if Chef has to fill the bottles now. If not, output "Not now".
"""

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("Water filling time" if a + b + c <= 1 else "Not now")
