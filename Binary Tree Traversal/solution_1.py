"""
Traversing of trees."""

# Pre-order traversal
def pre_order(node):
    """
    Preorder traversal."""
    if not node:
        return []
    res = [node.data]
    res += pre_order(node.left)
    res += pre_order(node.right)
    return res

# In-order traversal
def in_order(node):
    """
    Inorder traversal."""
    if not node:
        return []
    res = []
    res += in_order(node.left)
    res.append(node.data)
    res += in_order(node.right)
    return res

# Post-order traversal
def post_order(node):
    """
    Postorder traversal."""
    if not node:
        return []
    res = []
    res += post_order(node.left)
    res += post_order(node.right)
    res.append(node.data)
    return res

