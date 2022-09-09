# 589. N-ary Tree Preorder Traversal


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def helper(root: Node, arr):
    if root is None:
        return
    arr.append(root.val)
    for child in root.children:
        helper(child, arr)
    return arr


def preorder(root: Node) -> list[int]:
    return helper(root, [])

