# Jesus Carlos Martinez Gonzalez
# 07/07/2023
# Level order traversal (https://www.hackerrank.com/challenges/tree-level-order-traversal/problem)

"""
Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. 
In level-order traversal, nodes are visited level by level from left to right. 
Complete the function levelOrder and print the values in a single line separated by a space.
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

from collections import defaultdict

levels = defaultdict(list)


def levelOrder(root):
    i = 0
    level_order_helper(root, i)

    for values in levels.values():
        print(" ".join(map(str, values)), end=" ")


def level_order_helper(root, i):
    curr = i
    levels[curr].append(root.info)

    if root.left:
        level_order_helper(root.left, curr + 1)

    curr = i
    if root.right:
        level_order_helper(root.right, curr + 1)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
