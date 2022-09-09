# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, nodes: list[TreeNode]):
        out = []
        for node in nodes:
            if node.left:
                out.append(node.left)
            if node.right:
                out.append(node.right)
        return out

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return root
        output = [[root]]
        index = 0
        while True:
            next_level = self.helper(output[index])
            if not next_level:
                break
            output.append(next_level)
            index += 1
        for lst in output:
            for i in range(len(lst)):
                lst[i] = lst[i].val
        return output
