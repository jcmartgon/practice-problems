# Jesus Carlos Martinez Gonzalez
# 03/06/2023
# Detect HTML Attributes (https://www.hackerrank.com/challenges/html-attributes/problem)

"""
"""

import re

html_pattern = r"<([a-z0-9]+)((?:\s[a-z0-9]+=\"[^\"]+\")*)>"
attr_pattern = r"([a-z0-9]+)=\""


if __name__ == "__main__":
    n = int(input())
    data = {}
    for _ in range(n):
        text = input()
        if matches := re.findall(html_pattern, text):
            for match in matches:
                tag = match[0]
                if tag not in data:
                    data[tag] = []
                attributes = match[1].split()
                for attribute in attributes:
                    if attr_match := re.match(attr_pattern, attribute):
                        data[tag].append(attr_match.group(1))
    for key in data.keys():
        if data[key]:
            data[key] = set(data[key])
            data[key] = sorted(data[key])
    sorted_keys = sorted(data)
    for key in sorted_keys:
        attrs = data[key]
        print(f"{key}:{attrs}")
