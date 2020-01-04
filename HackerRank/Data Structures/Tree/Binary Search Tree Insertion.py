class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 


    def insert(self, val):
        if val < self.info:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)






