# Jesus Carlos Martinez Gonzalez
# 11/08/2023
# Podium finish (https://www.codechef.com/problems/PODIUM)

"""
Chef got his dream seat in Fl and secured a 3rd place in his debut race. He now wants to know the time
gap between him and the winner of the race.
You are his chief engineer and you only know the time gap between Chef and the runner up of the
race, given as A seconds, and the time gap between the runner up and the winner of the race, given as
B seconds.
Please calculate and inform Chef about the time gap between him and the winner of the race.
"""

for _ in range(int(input())):
    print(sum(list(map(int, input().split()))))
