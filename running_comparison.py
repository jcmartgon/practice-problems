# Jesus Carlos Martinez Gonzalez
# 29/12/2023
# Running comparison (https://www.codechef.com/problems/RUNCOMPARE)

"""
Alice and Bob recently got into running. and decided to compare how much they ran on different days.
They each ran for N days — on the t day, Alice ran Ai meters and Bob ran Bi meters.
On each day,
• Alice is unhappyif Bob ran strictly more than twice her distance, and happyotherwise.
• Similarly, Bob is unhappyif Alice ran strictly more than twice his distance, and happyotherwise.
For example, on a given day
• If Alice ran 200 meters and Bob ran 500, Alice would be unhappy but Bob would be happy.
• If Alice ran 500 meters and Bob ran 240, Alice would be happy and Bob would be unhappy.
• If Alice ran 300 meters and Bob ran 500, both Alice and Bob would be happy.
On how many of the N days were both Alice and Bob happy?
"""

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    # Your code goes here

    happy = 0

    for i in range(n):
        mx = max(a[i], b[i])
        mn = min(a[i], b[i])

        if mn * 2 >= mx:
            happy += 1

    print(happy)
