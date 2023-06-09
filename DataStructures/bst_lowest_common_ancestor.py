# Jesus Carlos Martinez Gonzalez
# 09/07/2023
# Binary Search Tree: Lowest Common Ancestor (https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem)

"""
You are given pointer to the root of the binary search tree and two values v1 and v2. You need to return the lowest common ancestor (LCA) of v1 and v2 in the binary search tree.
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


# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
"""


def lca(root, v1, v2):
    if (
        root.info > v1
        and root.info < v2
        or root.info > v2
        and root.info < v1
        or root.info in [v1, v2]
    ):
        return root
    if root.info > v1:
        return lca(root.left, v1, v2)
    else:
        return lca(root.right, v1, v2)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
