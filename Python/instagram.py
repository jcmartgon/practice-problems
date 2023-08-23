# Jesus Carlos Martinez Gonzalez
# 22/08/2023
# Instagram (https://www.codechef.com/problems/INSTAGRAM)

"""
Chef categorises an instagram account as spam, if, the followingcount of the account is more than 10
times the count of followers.
Given the following and followercount of an account as X and Y respectively. find whether it is a
spam account.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print("YES" if a > b * 10 else "NO")
