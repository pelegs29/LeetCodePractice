# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     find_p = find_q = saved = root
    #     while find_p == find_q:
    #         saved = find_p
    #
    #         if find_p.val < p.val:
    #             find_p = find_p.right
    #         elif find_p.val > p.val:
    #             find_p = find_p.left
    #
    #         if find_q.val < q.val:
    #             find_q = find_q.right
    #         elif find_q.val > q.val:
    #             find_q = find_q.left
    #
    #     return saved

    def lowestCommonAncestor(self, root, p, q):
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root
        return None
