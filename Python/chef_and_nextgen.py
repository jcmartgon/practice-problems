# Jesus Carlos Martinez Gonzalez
# 23/10/2023
# Chef and nextgen (https://www.codechef.com/problems/HELIUM3)

"""
Chef is currently working for a secret research group called NEXTGEN. While the rest of the world is still
in search of a way to utilize Helium-3 as a fuel, NEXTGEN scientists have been able to achieve 2 major
milestones:
1. Finding a way to make a nuclear reactor that will be able to utilize Helium-3 as a fuel
2. Obtaining every bit of Helium-3 from the moon's surface
Moving forward, the project requires some government funding for completion, which comes under
one condition: to prove its worth, the project should power Chefland by generating at least A units of
power each year for the next B years.
Help Chef determine whether the group will get funded assuming that the moon has X grams of
Helium-3 and 1 gram of Helium-3 can provide Y units of power.
"""

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("YES" if c * d >= a * b else "NO")
