# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def isSymmetric(root):
    # if tree is either empty or single node
    if root is None:
        return True
    if not root.left and not root.right:
        return True

    # Add root to queue two times so that
    # it can be checked if either one
    # child alone is NULL or not.
    q = [root, root]

    # To store two nodes for checking
    # their symmetry.
    leftNode = 0
    rightNode = 0

    while not len(q):
        # Remove first two nodes to
        # check their symmetry.
        leftNode = q[0]
        q.pop(0)

        rightNode = q[0]
        q.pop(0)

        # if both left and right nodes
        # exist, but have different
        # values-. inequality, return False
        if leftNode.val != rightNode.val:
            return False

        # append left child of left subtree
        # node and right child of right
        # subtree node in queue.
        if leftNode.left and rightNode.right:
            q.append(leftNode.left)
            q.append(rightNode.right)

        # If only one child is present
        # alone and other is NULL, then
        # tree is not symmetric.
        elif leftNode.left or rightNode.right:
            return False

        # append right child of left subtree
        # node and left child of right subtree
        # node in queue.
        if leftNode.right and rightNode.left:
            q.append(leftNode.right)
            q.append(rightNode.left)

        # If only one child is present
        # alone and other is NULL, then
        # tree is not symmetric.
        elif(leftNode.right or rightNode.left):
            return False

    return True
