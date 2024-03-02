# Jesus Carlos Martinez Gonzalez
# 01/03/2024
# Chef and remissness (https://www.codechef.com/problems/REMISS)

"""
The office where the Chef works, has two guards who count how many times a person enters into
the office building. Though the duty of a guard is 24 hours in a day, sometimes they fall asleep during
their duty and do not track the entry of a person in the office building. But one good thing is that they
never fall asleep at the same time. At least one of them remains awake and counts who enters into the
office.
Now the boss of Chef wants to calculate how many times the Chef has entered into the building. The
boss asked to the guard and they gave him two integers A and B, the count of first guard and second
guard respectively.
Help the boss to count the minimum and maximum number of times Chef could have entered into the
office building.
"""

for _ in range(int(input())):
    a, b = map(int, input().split())

    print(max(a, b), a + b)
