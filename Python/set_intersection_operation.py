# Jesus Carlos Martinez Gonzalez
# 11/06/2023
# set.intersection() operation (https://www.hackerrank.com/challenges/py-set-intersection/problem)

"""
You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. 
Your task is to find the total number of students who have subscribed to both newspapers.
"""

if __name__ == "__main__":
    n = int(input())
    english = set(input().split())
    m = int(input())
    french = set(input().split())

    print(len(english.intersection(french)))
