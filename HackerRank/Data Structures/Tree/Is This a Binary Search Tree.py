class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# wrong because it should return False for ex. 1 because 4 is in left subtree of 3
def check_binary_search_tree_(root):
    if root == None or (root.left == None and root.right == None):
        return True

    elif root.left and not root.right:
        return root.left.data < root.data and check_binary_search_tree_(root.left)

    elif root.right and not root.left:
        return root.right.data > root.data and check_binary_search_tree_(root.right)

    else:
        return root.left.data < root.data < root.right.data and check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)


# correct solution
def check_binary_search_tree_2(root):

    def helper(root, mi, ma):
        if root == None:
            return True
        elif root.data <= mi or root.data >= ma:
            return False
        else:
            return helper(root.left, mi, root.data) and helper(root.right, root.data, ma)
            
    return helper(root, -1, 10001)


# ex. 1
r = node(3)
r.left = node(2)
r.left.left = node(1)
r.left.right = node(4)
r.right = node(5)

print(check_binary_search_tree_(r))
print(check_binary_search_tree_2(r))
