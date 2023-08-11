# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Code fever (https://www.codechef.com/problems/FEVER)

"""
Chef is not feeling well today. He measured his body temperature using a thermometer and it came out
to be X OF.
A person is said to have fever if his body temperature is strictly greater than 98 OF.
Determine if Chef has fever or not.
"""

for _ in range(int(input())):
    print("YES" if int(input()) > 98 else "NO")
