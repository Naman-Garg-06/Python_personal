# INORDER TRAVERSAL
def printTree(root):
    if (root.left)!=None:
        printTree(root.left)
    print(root.data,end = ' ')
    if root.right:
        printTree(root.right)
