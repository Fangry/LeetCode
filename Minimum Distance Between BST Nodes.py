# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Misread and this code finds min difference between adjacent nodes
    def minDiffInBST(self, root):
        if root.left == None and root.right == None:
            return 100
        elif root.left == None:
            return min(abs(root.val - root.right.val), self.minDiffInBST(root.right))
        elif root.right == None:
            return min(abs(root.val - root.left.val), self.minDiffInBST(root.left))
        else:
            return min(abs(root.val - root.left.val),
                       abs(root.val - root.right.val),
                       self.minDiffInBST(root.left), self.minDiffInBST(root.right))

    # correct solution, inorder traverse
    def minDiffInBST2(self, root):
        def helper(root, low, high):
            if root == None:
                return high - low
            left = helper(root.left, low, root.val)
            right = helper(root.right, root.val, high)
            return min(left, right)
        return helper(root, -float('inf'), float('inf'))


s = Solution()

# testcase 1
bst = TreeNode(4)
bst.left = TreeNode(2)
bst.right = TreeNode(6)
bst.left.left = TreeNode(1)
bst.left.right = TreeNode(3)

# testcase 2
bst2 = TreeNode(90)
bst2.left = TreeNode(69)
bst2.left.left = TreeNode(49)
bst2.left.right = TreeNode(89)
bst2.left.left.right = TreeNode(52)

print(s.minDiffInBST2(bst2))
