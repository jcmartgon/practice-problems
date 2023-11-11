# Jesus Carlos Martinez Gonzalez
# 10/11/2023
# Second largest (https://www.codechef.com/problems/FLOW017)

"""
Three numbers A B and C are the inputs. Write a program to find second largest among them.
"""

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst = [x for x in lst if x not in [max(lst), min(lst)]]
    print(lst[0])
