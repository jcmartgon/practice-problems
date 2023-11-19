# Jesus Carlos Martinez Gonzalez
# 18/11/2023
# Rcb and playoffs (https://www.codechef.com/problems/RCBPLAY)

"""
Team RCB has earned X points in the games it has played so far in this year's IPL. To qualify for the
playoffs they must earn at least a total of Y points. They currently have Z games left, in each game
they earn 2 points for a win, 1 point for a draw, and no points for a loss.
Is it possible for RCB to qualify for the playoffs this year?
"""


for _ in range(int(input())):
    current_points, min_required, matches_left = map(int, input().split())
    print("YES" if current_points + matches_left * 2 >= min_required else "NO")
