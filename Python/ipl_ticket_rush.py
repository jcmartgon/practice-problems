# Jesus Carlos Martinez Gonzalez
# 03/08/2023
# IPL ticket rush (https://www.codechef.com/problems/IPLTRSH)

"""
DAIICT college students want to attend an IPL match.
A total of N students from the college want to go while only M tickets are available for the match.
Determine how many students won't be able to book tickets.
"""

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(x - y if x >= y else 0)
