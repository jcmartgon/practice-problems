# Jesus Carlos Martinez Gonzalez
# 23/08/2023
# Volume control (https://www.codechef.com/problems/VOLCONTROL)

"""
Chef is watching TV. The current volume of the TV is X. Pressing the volume up button of the TV
remote increases the volume by 1 while pressing the volume down button decreases the volume by 1.
Chef wants to change the volume from Xto Y. Find the minimum number of button presses required
to do so.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(abs(a - b))
