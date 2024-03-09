# Jesus Carlos Martinez Gonzalez
# 06/03/2024
# World chess championship (https://www.codechef.com/problems/WCC)

"""
The World Chess Championship 2022 is about to start. 14 Classical games will be played between Chef
and Carlsen in the championship, where each game has one of three outcomes — it can be won by
Carlsen, won by Chef, or it can be a draw. The winner of a game gets 2 points, and the loser gets O
points. If its a draw, both players get 1 point each.
The total prize pool of the championship is 100 • X. At end of the 14 Classical games, if one player has
strictly more points than the other, he is declared the champion and gets 60 • X as his prize money,
and the loser gets 40 • X.
Ifthe total points are tied, then the defending champion Carlsen is declared the winner. However, if
this happens, the winner gets only 55 • X, and the loser gets 45 • X.
Given the results of all the 14 games, output the prize money that Carlsen receives.
The results are given as a string of length 14 consisting of the characters c, N, and D.
•
•
•
c denotes a victory by Carlsen.
N denotes a victory by Chef.
D denotes a draw.
"""

for _ in range(int(input())):
    x = int(input())

    score = input()
    winner = 0

    for c in score:
        match c:
            case "C":
                winner += 1
            case "N":
                winner -= 1

    if winner > 0:
        print(x * 60)
    elif winner == 0:
        print(x * 55)
    else:
        print(x * 40)
