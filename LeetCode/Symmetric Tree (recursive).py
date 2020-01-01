# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetric2(root.left, root.right)

    def isSymmetric2(self, r1, r2):
        if r1 is None and r2 is None:
            return True
        elif r1 is None or r2 is None:
            return False
        return (r1.val == r2.val) and self.isSymmetric2(r1.left, r2.right) and self.isSymmetric2(r1.right, r2.left)
