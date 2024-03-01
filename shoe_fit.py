# Jesus Carlos Martinez Gonzalez
# 29/02/2024
# Shoe fit (https://www.codechef.com/problems/SHOEFIT)

"""
You have three shoes of the same size lying around. Each shoe is either a left shoe (represented using 0
) or a right shoe (represented using 1). Given A. B. C representing the information for each shoe, find
out whether you can go out now, wearing one left shoe and one right shoe.
"""

for _ in range(int(input())):
    shoes = list(map(int, input().split()))

    print(1 if 0 in shoes and 1 in shoes else 0)
