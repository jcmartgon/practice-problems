# Jesus Carlos Martinez Gonzalez
# 30/05/2023
# Detecting Valid Latitude and Longitude Pairs (https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem)

"""
Given a line of text which possibly contains the latitude and longitude of a point, can you use regular expressions to identify the latitude and longitude referred to (if any)?
"""

import re

coord_pattern = r"\([+-]?([1-9]\d*(?:\.\d+)?), [+-]?([1-9]\d*(?:\.\d+)?)\)"

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        coord = input()
        if match := re.fullmatch(coord_pattern, coord):
            x, y = map(float, match.groups())
            if x <= 90 and y <= 180:
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
