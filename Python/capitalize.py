# Jesus Carlos Martinez Gonzalez
# 31/05/2023
# Capitalize (https://www.hackerrank.com/challenges/capitalize/problem)

"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    caps = ""
    for i, c in enumerate(s):
        if i == 0:
            caps += c.upper()
        else:
            if s[i - 1] == " ":
                caps += c.upper()
            else:
                caps += c
    print(caps)
    return caps


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    fptr.write(result + "\n")

    fptr.close()
