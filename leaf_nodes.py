# LEAF-NODES
def printLeafNodes(root, minimum_depth):
    if root.left:
        minimum_depth = printLeafNodes(root.left, minimum_depth)
    if root.right:
        minimum_depth = printLeafNodes(root.right, minimum_depth)
    if root.left is None and root.right is None:
        print(root.data,end = " ")
