# Jesus Carlos Martinez Gonzalez
# 22/11/2023
# Lazy chef (https://www.codechef.com/problems/LAZYCHF)

"""
Chef is a very lazy person. Whatever work is supposed to be finished in units of time, he finishes it in
m * units of time. But there is always a limit to laziness, so he delays the work by at max d units of
time. Given x, m, d find the maximum time taken by Chef to complete the work.
"""


for _ in range(int(input())):
    task_time, lazy_extra, lazy_limit = map(int, input().split())

    print(min(task_time * lazy_extra, task_time + lazy_limit))
