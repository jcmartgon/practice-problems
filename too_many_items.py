# Jesus Carlos Martinez Gonzalez
# 10/11/2023
# Too many items (https://www.codechef.com/problems/POLYBAGS)

"""
Chef bought N items from a shop. Although it is hard to carry all these items in hand, so Chef has to
buy some polybags to store these items.
1 polybag can contain at most 10 items. What is the minimum number of polybags needed by Chef?
"""

for _ in range(int(input())):
    print((int(input()) + 9) // 10)
