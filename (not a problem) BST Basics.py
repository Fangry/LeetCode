class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorderPrint(self):
        if self.left != None:
            self.left.inorderPrint()
        print(self.val)
        if self.right != None:
            self.right.inorderPrint()

    def insert(self, node):
        if self is None:
            self = node
        else:
            if node.val > self.val:
                if self.right is None:
                    self.right = node
                else:
                    self.right.insert(node)
            else:
                if self.left is None:
                    self.left = node
                else:
                    self.left.insert(node)

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def sortedLstToBST(lst):
    if lst == []:
        return None
    midIndex = len(lst)//2

    # one less node every iteration because that node becomes the root node
    root = BSTNode(lst[midIndex])
    root.left = sortedLstToBST(lst[:midIndex])
    root.right = sortedLstToBST(lst[midIndex + 1:])
    return root


def ifNodeExists(root, target):
    if root == None:
        return False
    if root.val == target:
        return True
    else:
        return ifNodeExists(root.left, target) or ifNodeExists(root.right, target)


# find distance (number of edges) from root to a target node, if target value doesn't exist, return -1
def findDistance(root, target):
    def helper(root):
        if target == root.val:
            return 0
        elif target > root.val:
            return 1 + helper(root.right)
        else:
            return 1 + helper(root.left)

    if ifNodeExists(root, target):
        return helper(root)
    else:
        return -1


n = sortedLstToBST([1, 2, 3, 4, 5, 6, 7])
n.display()
