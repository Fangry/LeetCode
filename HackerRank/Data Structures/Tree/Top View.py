'''
ex. 
        1
      /   \
    2       3
      \   
        4  
          \
            5
             \
               6
Top view of the above binary tree is
2 1 3 6
'''


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None


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


# 1st attempt
# doesn't work bc. the inner tree can branch out longer than the outermost layer
def topView(root):

    def helper1(root):
        if root:
            print(root.info, '', end='')
            if root.left:
                helper1(root.left)

    def helper2(root):
        if root:
            print(root.info, '', end='')
            if root.right:
                helper2(root.right)

    helper1(root.left)
    print(root.info, '', end='')
    helper2(root.right)


# 2nd attempt
# basically, each hd (horizontal distance from root node) is s spot that can hold one node
# ex. ... -2 -1 0 (root node) 1 2 ...
def topView2(root):
    top = {}

    def helper(root, hd):
        if root == None:
            return
        if hd not in top:
            top[hd] = root.info

        helper(root.left, hd-1)
        helper(root.right, hd+1)

    helper(root, 0)
    for k in sorted(top.keys()):
        print(top[k], end=' ')


# different approach
def topView3(root, side=0):
    if root == None:
        return 0
    if side == 0 or side == -1:
        topView3(root.left, side=-1)

    print(root.info)

    if side == 0 or side == 1:
        topView3(root.right, side=1)
    return
