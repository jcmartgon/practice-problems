# Jesus Carlos Martinez Gonzalez
# 29/06/2023
# Decorators 2 - Name Directory (https://www.hackerrank.com/challenges/decorators-2-name-directory/problem)

"""
Let's use decorators to build a name directory! You are given some information about N people. 
Each person has a first name, last name, age and sex. 
Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. 
For two people of the same age, print them in the order of their input.
"""

import operator


def person_lister(f):
    def inner(people):
        sorted_people = sorted(people, key=operator.itemgetter(2))
        formatted_names = [f(person) for person in sorted_people]
        return formatted_names

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == "__main__":
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep="\n")
