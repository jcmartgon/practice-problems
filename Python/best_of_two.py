# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Best of two (https://www.codechef.com/problems/BESTOFTWO)

"""
Chef took an examination two times. In the first attempt. he scored X marks while in the second
attempt he scored Y marks. According to the rules of the examination, the best score out of the two
attempts will be considered as the final score.
Determine the final score of the Chef.
"""

t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    print(max(X, Y))
