# Jesus Carlos Martinez Gonzalez
# 18/03/2024
# Dark Light (https://www.codechef.com/problems/DARLIG)

"""
Tonmoy has a special torch. The torch has 4 levels numbered 1 to 4 and 2 states (On and Off). Levels
I, 2, and 3 correspond to the On state while level 4 corresponds to the Off state.
The levels of the torch can be changed as:
• Level 1 changes to level 2.
• Level 2 changes to level 3.
• Level 3 changes to level 4.
• Level 4 changes to level 1.
Given the initial state as K and the number of changes made in the levels as N, find the final state of
the torch. If the final state cannot be determined, print Ambiguous instead.
"""

for _ in range(int(input())):
    changes, state = [int(x) for x in input().split()]

    if not state:
        if changes % 4 == 0:
            print("Off")
        else:
            print("On")
    else:
        if changes % 4 == 0:
            print("On")
        else:
            print("Ambiguous")
