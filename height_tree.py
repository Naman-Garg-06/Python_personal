# HEIGHT OF THE TREE
def maxDepth(root):
    if root.left == None and root.right == None:
        return 1
    left = right = 0
    if root.left:
        left = root.left.maxDepth()
    if root.right:
        right = root.right.maxDepth()
    height = max(left,right) +1
    return height
