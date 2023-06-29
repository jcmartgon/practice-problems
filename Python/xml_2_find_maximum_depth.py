# Jesus Carlos Martinez Gonzalez
# 29/06/2023
# XML 2 - Find the Maximum Depth (https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem)

"""
You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 0.
"""

import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    maxdepth = get_element_depth(elem)


def get_element_depth(element):
    if len(element) == 0:
        return 0
    else:
        child_depths = [get_element_depth(child) for child in element]
        return max(child_depths) + 1


if __name__ == "__main__":
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
