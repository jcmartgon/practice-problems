# Jesus Carlos Martinez Gonzalez
# 18/12/2023
# Bells of pilgrimage (https://www.codechef.com/problems/PILBELLS)

"""
The Child of Prophecy has embarked on a journey to save the land of the Fae.
On her journey, she must ring N Bells of Pilgrimage.
The Child of Prophecy has an initial mana level of P. After that:
• Each of the first X bells she rings will increase her mana level by 10.
• Each of the remaining bells will increase her mana level by 5.
• As a bonus, once the final bell is rung. her mana level will increase by a further 20.
K bells have been rung so far. What is the current mana level of the Child of Prophecy?
"""

for _ in range(int(input())):
    total_bells, special_bells, current_bells, initial_mana = map(int, input().split())

    current_mana = initial_mana
    non_special_bells = total_bells - special_bells

    if current_bells >= total_bells:
        current_mana += 20 + special_bells * 10 + non_special_bells * 5

    elif current_bells >= special_bells:
        current_mana += special_bells * 10 + (current_bells - special_bells) * 5

    else:
        current_mana += current_bells * 10

    print(current_mana)
