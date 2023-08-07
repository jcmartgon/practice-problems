# Jesus Carlos Martinez Gonzalez
# 06/08/2023
# Reach on time (https://www.codechef.com/problems/TIMELY)

"""
Chef has recently moved into an apartment. It takes 30 minutes for Chef to reach office from the
apartment.
Chef left for the office X minutes before Chef was supposed to reach. Determine whether or not Chef
will be able to reach on time.
"""

t = int(input())
for _ in range(t):
    print("YES" if int(input()) >= 30 else "NO")
