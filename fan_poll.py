# Jesus Carlos Martinez Gonzalez
# 04/04/2024
# Fan poll (https://www.codechef.com/problems/FIZZBUZZ2301)

"""
Chef Sports conducted a fan poll to find out who their fans thought was the best captain.
The three players nominated were Dhoni, Rohit, and Kohli. They received A, B, and C votes,
respectively.
Find out whether Dhoni won the poll, i.e. if he received the maximum number of votes.
Note: It is guaranteed that no two players received the same number of votes.
"""

votes = [int(x) for x in input().split()]

print("YES" if votes[0] == max(votes) else "NO")
