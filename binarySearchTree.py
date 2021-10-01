class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addToTree(self,data):
        new_node = node(data)
        while True:
            if new_node.data <= self.data:
                if self.left == None:
                    self.left = new_node
                    break
                else:
                    self = self.left
            else:
                if self.right == None:
                    self.right = new_node
                    break
                else:
                    self = self.right

    def printTree(self):
        if (self.left)!=None:
            self.left.printTree()
        print(self.data,end = ' ')
        if self.right:
            self.right.printTree()
root = node(12)
root.addToTree(6)
root.addToTree(14)
root.addToTree(3)
root.addToTree(7)
root.addToTree(13)

root.printTree()
print()