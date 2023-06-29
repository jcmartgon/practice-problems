# Jesus Carlos Martinez Gonzalez
# 28/06/2023
# HTML Parser Part 2 (https://www.hackerrank.com/challenges/html-parser-part-2/problem)

"""
You are given an HTML code snippet of N lines.
Your task is to print the single-line comments, multi-line comments and the data.
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data", data, sep="\n")


if __name__ == "__main__":
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += "\n"

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
