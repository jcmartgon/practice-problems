# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Learning SQL (https://www.codechef.com/problems/LEARNSQL)

"""
Chef has recently started learning from the new CodeChef SQL course.
He has a table which initially has R rows and C columns. He then adds E extra rows to it. How many
total cells does he have finally?
"""

x, y, z = map(int, input().split())
print((x + z) * y)
