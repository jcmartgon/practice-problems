# Jesus Carlos Martinez Gonzalez
# 10/08/2023
# Enough space (https://www.codechef.com/problems/ENSPACE)

"""
Chefs computer has N GB of free space. He wants to save X files, each of size 1 GB and Y files, each
of size 2 GB on his computer. Will he be able to do so?
Chef can save all the files on his computer only if the total size of the files is less than or equal to the
space available on his computer.
"""

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print("YES" if y + z * 2 <= x else "NO")
