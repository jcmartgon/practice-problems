# Jesus Carlos Martinez Gonzalez
# 06/03/2024
# Back to campus (https://www.codechef.com/problems/MINDAYSRET)

"""
Finally, College has started calling students back to campus. There are so many students and thus due
to some safety measures the college can't call back all the students on the same day. It currently has
the capacity of screening K students on a single day. There is a total of N students. What's the
minimum number of days required for all the students to be back on the campus?
"""

from math import ceil

for _ in range(int(input())):
    total_students, recall_capacity = map(int, input().split())
    print(ceil(total_students / recall_capacity))
