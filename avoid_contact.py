# Jesus Carlos Martinez Gonzalez
# 05/01/2024
# Avoid contact (https://www.codechef.com/problems/AVOIDCONTACT)

"""
A hostel has N rooms in a straight line. It has to accommodate X people. Unfortunately, out of these
X people, Y of them are infected with chickenpox. Due to safety norms. the following precaution must
be taken:
• No person should occupy a room directly adjacent to a room occupied by a chickenpox-infected
person. In particular, two chickenpox-infected people cannot occupy adjacent rooms.
For example, if room 4 has a chickenpox-infected person, then nobody should occupy rooms 3 and 5.
Similarly, if room 1 has a chickenpox-infected person then nobody should occupy room 2.
What's the minimum value of N for which all the people can be accommodated in the hostel, following
the above condition?
"""

for _ in range(int(input())):
    total, infected = map(int, input().split())
    healthy = total - infected if infected != total else -1

    print(infected * 2 + healthy)
