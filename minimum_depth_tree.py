# MINIMUM DEPTH
def min_depth(root,depth):
    root.depth = depth
    if root.left:
        min_depth(root.left,depth+1)
    if root.right:
        min_depth(root.right,depth+1)

min_depth(root,0)
