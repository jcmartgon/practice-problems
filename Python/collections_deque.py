# Jesus Carlos Martinez Gonzalez
# 08/06/2023
# Collections.deque() (https://www.hackerrank.com/challenges/py-collections-deque/problem)

"""
Perform append, pop, popleft and appendleft methods on an empty deque d.
"""

from collections import deque

if __name__ == "__main__":
    d = deque()
    n = int(input())
    for _ in range(n):
        command = input()
        try:
            command, value = command.split()
        except ValueError:
            pass
        match command:
            case "append":
                d.append(value)
            case "pop":
                d.pop()
            case "appendleft":
                d.appendleft(value)
            case "popleft":
                d.popleft()
            case _:
                raise ValueError("Invalid command")
    print(" ".join(d))