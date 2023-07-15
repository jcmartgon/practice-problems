# Jesus Carlos Martinez Gonzalez
# 14/07/2023
# Tree: Top View (https://www.hackerrank.com/challenges/tree-top-view/problem)

"""
Given a pointer to the root of a binary tree, print the top view of the binary tree.

The tree as seen from the top the nodes, is called the top view of the tree.
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from queue import Queue


def topView(root):
    if not root:
        return

    columns = {}

    queue = Queue()
    queue.put((root, 0))

    while queue.qsize():
        node, column = queue.get()

        if column not in columns:
            columns[column] = node.info

        if node.left:
            queue.put((node.left, column - 1))

        if node.right:
            queue.put((node.right, column + 1))

    for column in sorted(columns.keys()):
        print(columns[column], end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
