# Jesus Carlos Martinez Gonzalez
# 28/06/2023
# HTML Parser Part 1 (https://www.hackerrank.com/challenges/html-parser-part-1/problem)

"""
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")


if __name__ == "__main__":
    n = int(input())

    html_code = ""
    for _ in range(n):
        html_code += input()

    parser = MyHTMLParser()
    parser.feed(html_code)
