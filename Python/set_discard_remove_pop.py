# Jesus Carlos Martinez Gonzalez
# 08/06/2023
# set.discard(), .remove(), & .pop() (https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem)

"""
You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.
"""

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        command = input()
        try:
            command, value = command.split()      
            value = int(value)
        except ValueError:
            pass
        match command:
            case "pop":
                s.pop()
            case "remove":
                s.remove(value)
            case "discard":
                s.discard(value)
            case _:
                raise ValueError("Invalid Command")
    print(sum(s))
