# Jesus Carlos Martinez Gonzalez
# 31/05/2023
# Find HackerRank (https://www.hackerrank.com/challenges/find-hackerrank/problemS)

"""
At HackerRank, we always want to find out how popular we are getting every day and have scraped conversations from popular sites. Each conversation fits in 1 line and there are N such conversations. Each conversation has at most 1 word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation:

1. Starts with hackerrank
2. Ends with hackerrank
3. Start and ends with hackerrank
"""

import re


def main():
    n = int(input())
    for _ in range(n):
        pan_text = input()
        print(pattern_pos("hackerrank", pan_text))


def pattern_pos(pattern, text):
    """Retuns relative position of pattern in text"""
    if re.search(rf"^{pattern}$", text):  # Pattern is text
        return 0
    elif re.search(rf"^{pattern}.+", text):  # Pattern at start of text
        return 1
    elif re.search(rf".+{pattern}$", text):  # Pattern at end of text
        return 2
    elif re.search(rf".+{pattern}.+", text):  # Pattern in between text
        return -1
    else:  # Pattern not in text
        return -2


if __name__ == "__main__":
    main()
