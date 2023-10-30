# Jesus Carlos Martinez Gonzalez
# 29/10/2023
# The three topics (https://www.codechef.com/problems/THREETOPICS)

"""
The Chef has reached the finals of the Annual Inter-school Declamation contest.
For the finals, students were asked to prepare 10 topics. However, Chef was only able to prepare three
topics, numbered A, B and C— he is totally blank about the other topics. This means Chef can only
win the contest if he gets the topics A, B or C to speak about.
On the contest day. Chef gets topic X. Determine whether Chef has any chances of winning the
competition.
Print "Yes" if it is possible for Chef to win the contest else print "No".
You may print each character of the string in either uppercase or lowercase (for example. the strings
YES, yes, Yes, and YES will all be treated as identical).
"""

lst = list(map(int, input().split()))
print("YES" if lst[3] in lst[:2] else "NO")
