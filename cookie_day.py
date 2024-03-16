# Jesus Carlos Martinez Gonzalez
# 15/03/2024
# Cookie day (https://www.codechef.com/problems/ADVITIYA3)

"""
A very caring mother has N cookie jars with her. Each jar contains a different type of cookie.
There are Ai cookies in the ith jar.
The mother wanted to give some cookies to her K children, and she decided to only distribute cookies
of a single type. That is, she'll choose exactly one of the N jars and distribute the cookies within it.
She'd like to ensure a couple of things:
• Each child should receive at least I cookie.
• Each child should also receive an equal number of cookies, in the spirit of fairness.
Under the above two conditions, what is the minimum number of "wasted" cookies, i.e. cookies that
remain in the chosen jar after distribution?
If it is not possible to give out any cookies at all, print —1 instead.
"""

for _ in range(int(input())):
    jars, children = map(int, input().split())
    cookies_per_jar = [int(x) for x in input().split()]

    min_wasted = max(cookies_per_jar)
    enough = False

    for jar in cookies_per_jar:
        if jar >= children:
            enough = True
            min_wasted = min(min_wasted, jar % children)

    print(min_wasted if enough else -1)
