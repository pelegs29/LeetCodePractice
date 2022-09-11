# 98. Validate Binary Search Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, None, None)

    def isValid(self, root: TreeNode, left: TreeNode, right: TreeNode) -> bool:
        if root is None:
            return True
        if left is not None and root.val <= left.val:
            return False
        if right is not None and root.val >= right.val:
            return False
        return self.isValid(root.right, root, right) and self.isValid(root.left, left, root)


# inorder traversal and check
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         in_order = self.inorderTraversal(root)
#         prev = in_order[0]
#         for i in range(1, len(in_order) - 1):
#             curr = in_order[i]
#             if prev >= curr:
#                 return False
#             prev = curr
#         return True
#
#     def inorderTraversal(self, root):
#         res = []
#         if root:
#             res = self.inorderTraversal(root.left)
#             res.append(root.val)
#             res = res + self.inorderTraversal(root.right)
#         return res
