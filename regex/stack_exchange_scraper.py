# Jesus Carlos Martinez Gonzalez
# 30/05/2023
# Build a Stack Exchange Scraper

"""
Stack Exchange is an information power-house, which contains libraries of crowdsourced problems (with answers) across a large number of topics which are as diverse as electronics, cooking , programming, etc.
We are greatly interested in crawling and scraping as many questions, as we can, from stack-exchange. This is an example of a question library page from stack-exchange.

Your task will be, to scrape the questions from each library page, in the order in which they are listed. You will be provided with the markup of question listing pages, from which you need to detect:
(1) Identifier (2) Question text (which is on the Hyperlink to the question) (3) How long ago the question was asked.
"""

import re
import sys

text = sys.stdin.read()

id_pattern = r'<h3><a href="/questions/(\d*)'
question_pattern = r'class="question-hyperlink">(.*)</a>'
date_pattern = r'<span title=".*" class="relativetime">(.*)<'

ids = re.findall(id_pattern, text)
questions = re.findall(question_pattern, text)
dates = re.findall(date_pattern, text)

data = zip(ids, questions, dates)

for i in data:
    print(";".join(list(i)))
