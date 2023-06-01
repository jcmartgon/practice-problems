# Jesus Carlos Martinez Gonzalez
# 01/06/2023
# HackerRank Language (https://www.hackerrank.com/challenges/hackerrank-language/problem)

"""
Every submission at HackerRank has a field called language which indicates the programming language which a hacker used to code his solution.

C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC

Sometimes, error-prone API requests can have an invalid language field. Could you find out if a given submission has a valid language field or not?
"""

import re

langs = [
    "C",
    "CPP",
    "JAVA",
    "PYTHON",
    "PERL",
    "PHP",
    "RUBY",
    "CSHARP",
    "HASKELL",
    "CLOJURE",
    "BASH",
    "SCALA",
    "ERLANG",
    "CLISP",
    "LUA",
    "BRAINFUCK",
    "JAVASCRIPT",
    "GO",
    "D",
    "OCAML",
    "R",
    "PASCAL",
    "SBCL",
    "DART",
    "GROOVY",
    "OBJECTIVEC",
]

"""
Intentionally used regex since its a regex problem but the following would have been better

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        api_id, lang_string = input().split()
        print("VALID" if lang_string in langs else "INVALID")
"""

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        valid = False
        api_id, lang_string = input().split()
        for lang in langs:
            if match := re.fullmatch(rf"{lang}", lang_string):
                valid = True
                print("VALID")
                break
        if not valid:
            print("INVALID")
