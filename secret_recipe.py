# Jesus Carlos Martinez Gonzalez
# 20/12/2023
# Secret recipe (https://www.codechef.com/problems/CHEFRUN)

"""
Chef and his competitor Kefa own two restaurants located at a straight road. The position of Chefs
restaurant is Xl, the position of Kefa's restaurant is X2.
Chef and Kefa found out at the same time that a bottle with a secret recipe is located on the road
between their restaurants. The position of the bottle is X3.
The cooks immediately started to run to the bottle. Chef runs with speed VI, Kefa with speed V2.
Your task is to figure out who reaches the bottle first and gets the secret recipe (of course, it is possible
that both cooks reach the bottle at the same time).
"""

for _ in range(int(input())):
    chef_position, kefa_position, formula_position, chef_speed, kefa_speed = map(
        int, input().split()
    )

    chef_time = abs(formula_position - chef_position) / chef_speed
    kefa_time = abs(formula_position - kefa_position) / kefa_speed

    print(
        "Chef" if chef_time < kefa_time else "Kefa" if kefa_time < chef_time else "Draw"
    )
