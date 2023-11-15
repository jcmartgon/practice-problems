# Jesus Carlos Martinez Gonzalez
# 15/11/2023
# Reach fast (https://www.codechef.com/problems/REACHFAST)

"""
Chef is standing at coordinate A while Chefina is standing at coordinate B.
In one step, Chef can increase or decrease his coordinate by at most K.
Determine the minimum number of steps required by Chef to reach Chefina.
"""


from math import ceil

for _ in range(int(input())):
    chef, chefina, max_steps = map(int, input().split())
    print(ceil(abs(chef - chefina) / max_steps))
