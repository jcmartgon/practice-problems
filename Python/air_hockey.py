# Jesus Carlos Martinez Gonzalez
# 13/08/2023
# Air hockey (https://www.codechef.com/problems/AIRHOCKEY)

"""
Alice is playing Air Hockey with Bob. The first person to earn seven points wins the match. Currently,
Alice's score is A and Bob's score is B.
Charlie is eagerly waiting for his turn. Help Charlie by calculating the minimum number of points that
will be further scored in the match before it ends.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(7 - max(a, b))
