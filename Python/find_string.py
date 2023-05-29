# Jesus Carlos Martinez Gonzalez
# 28/05/2023
# Find a String (https://www.hackerrank.com/challenges/find-a-string/problem)

"""
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
"""

# Decided not to use regex, to practice recurrsion


def count_substring(string, sub_string):
    """Returns amount of times sub_string is in string"""
    i = string.find(sub_string)
    if i == -1:
        return 0
    return 1 + count_substring(string[i + 1 :], sub_string)


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
