# Jesus Carlos Martinez Gonzalez
# 30/05/2023
# HackerRank Tweets (https://www.hackerrank.com/challenges/hackerrank-tweets/problem)

"""
Increasing popularity of hackerrank can be seen in tweets like

- I love #hackerrank
- I just scored 27 points in the Picking Cards challenge on #HackerRank
- I just signed up for summer cup @hackerrank
Given a set of most popular tweets, your task is to find out how many of those tweets has the string hackerrank in it.
"""

import re

hr_pattern = r"hackerrank"

if __name__ == "__main__":
    n = int(input())
    count = 0
    for _ in range(n):
        tweet = input()
        if match := re.search(hr_pattern, tweet.lower()):
            count += 1
    print(count)
