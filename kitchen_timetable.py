# Jesus Carlos Martinez Gonzalez
# 15/03/2024
# Kitchen timetable (https://www.codechef.com/problems/KTTABLE)

"""
There are N students living in the dormitory of Berland State University. Each of them sometimes wants
to use the kitchen, so the head of the dormitory came up with a timetable for kitchen's usage in order
to avoid the conflicts:
• The first student starts to use the kitchen at the time O and should finish the cooking not later than at
the time A1.
• The second student starts to use the kitchen at the time A1 and should finish the cooking not later
than at the time A2.
• And so on.
• The N-th student starts to use the kitchen at the time Aw and should finish the cooking not later
than at the time AN
The holidays in Berland are approaching, so today each of these N students wants to cook some
pancakes. The i-th student needs Bi units of time to cook.
The students have understood that probably not all of them will be able to cook everything they want.
How many students will be able to cook without violating the schedule?
"""

for _ in range(int(input())):
    students = int(input())
    assigned_times = [0]
    assigned_times.extend([int(x) for x in input().split()])
    required_times = [int(x) for x in input().split()]

    available_times = [
        assigned_times[i] - assigned_times[i - 1] for i in range(1, students + 1)
    ]

    completed = 0

    for student in range(students):
        if available_times[student] >= required_times[student]:
            completed += 1

    print(completed)
