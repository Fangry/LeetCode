class Node:
    def __init__(self, info):
        self.left = None
        self.right = None
        self.info = info


def preOrder(root):
    if root:
        print(root.info, '', end='')
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)


n = Node(1)
n.right = Node(2)
n.right.right = Node(5)
n.right.right.left = Node(3)
n.right.right.left.right = Node(4)
n.right.right.right = Node(6)

preOrder(n)
