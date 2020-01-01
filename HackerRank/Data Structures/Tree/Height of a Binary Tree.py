def height(root):

    def helper(curr, h):
        if curr == None or (curr.left == None and curr.right == None):
            return h
        elif curr.left == None:
            return helper(curr.right, h+1)
        elif curr.right == None:
            return helper(curr.left, h+1)
        else:
            return max(helper(curr.left, h+1), helper(curr.right, h+1))

    return helper(root, 0)


# simplified version
def height2(root):

    def helper(curr, h):
        if curr == None:
            return h
        else:
            return max(helper(curr.left, h+1), helper(curr.right, h+1))

    return helper(root, 0)-1


# iterative solution using queue
def height3(root):
    if root == None:
        return 0

    q = [root]  # initialize queue
    h = -1

    while True:
        nodeCount = len(q)
        if nodeCount == 0:
            return h
        h += 1

        # dequeue all nodes of current level & enqueue all nodes of next level
        for i in range(len(q)):
            curr = q[0]
            q.pop(0)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
