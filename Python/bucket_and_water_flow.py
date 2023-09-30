# Jesus Carlos Martinez Gonzalez
# 29/09/2023
# Bucket and water flow (https://www.codechef.com/problems/WATERFLOW)

"""
Alice has a bucket of water initially having W litres of water in it. The maximum capacity of the bucket
is X liters.
Alice turned on the tap and the water starts flowing into the bucket at a rate of Y litres/hour. She left
the tap running for exactly Z hours. Determine whether the bucket has been overflown, filled exactly,
or is still left unfilled.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    total = a + c * d
    if total > b:
        print("overFlow")
    elif total < b:
        print("Unfilled")
    else:
        print("filled")
