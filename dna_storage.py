# Jesus Carlos Martinez Gonzalez
# 23/11/2023
# Dna storage (https://www.codechef.com/problems/DNASTORAGE)

"""
Chef is a very lazy person. Whatever work is supposed to be finished in units of time, he finishes it in
m * units of time. But there is always a limit to laziness, so he delays the work by at max d units of
time. Given x, m, d find the maximum time taken by Chef to complete the work.
"""


codex = {"00": "A", "01": "T", "10": "C", "11": "G"}

for _ in range(int(input())):
    n = int(input())
    s = input()
    new = ""

    for i in range(0, len(s), 2):
        new += codex[s[i] + s[i + 1]]

    print(new)
