def levelOrder(root):
    q = [root]

    while q:
        temp = q[0]
        q.pop(0)
        print(temp, '', end='')
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
