# Jesus Carlos Martinez Gonzalez
# 26/05/23
# Lists (https://www.hackerrank.com/challenges/python-lists/problem)

"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""

if __name__ == "__main__":
    N = int(input())

    lst = []

    # Iterate over user input
    for _ in range(N):
        cmd = input().split()
        method = cmd[0]

        # Execute method on list based on cmd
        if method == "insert":
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif method == "print":
            print(lst)
        elif method == "remove":
            lst.remove(int(cmd[1]))
        elif method == "append":
            lst.append(int(cmd[1]))
        elif method == "sort":
            lst.sort()
        elif method == "pop":
            lst.pop()
        elif method == "reverse":
            lst.reverse()
