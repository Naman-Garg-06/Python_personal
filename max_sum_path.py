# MAXIMUM SUM PATH
def max_sum_path(root, temp_value):
    root.sum_till_node = temp_value + root.data
    if root.left:
        max_sum_path(root.left, root.sum_till_node)
    if root.right:
        max_sum_path(root.right, root.sum_till_node)
# returns maximum sum of the path from root to leaf.
