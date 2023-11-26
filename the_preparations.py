# Jesus Carlos Martinez Gonzalez
# 25/11/2023
# The preparations (https://www.codechef.com/problems/SUPCHEF)

"""
Chef has an exam which will start exactly M minutes from now. However, instead of preparing for his
exam, Chef started watching Season-I of Superchef. Season-I has N episodes. and the duration of
each episode is K minutes.
Will Chef be able to finish watching season-I strictly before the exam starts?
Note: Please read the explanations of the sample test cases carefully.
"""


for _ in range(int(input())):
    minutes_before_exam, number_episodes, episode_length = map(int, input().split())

    print("YES" if number_episodes * episode_length < minutes_before_exam else "NO")
