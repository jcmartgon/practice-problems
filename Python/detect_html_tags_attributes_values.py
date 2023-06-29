# Jesus Carlos Martinez Gonzalez
# 28/06/2023
# Detect HTML tags, attributes and attribute values (https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem)

"""
You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")


if __name__ == "__main__":
    n = int(input())

    html_code = ""
    for _ in range(n):
        html_code += input()

    parser = MyHTMLParser()
    parser.feed(html_code)
