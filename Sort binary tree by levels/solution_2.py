"""
Sort binary tree by levels."""

from collections import deque

def tree_by_levels(node):
    """
    Sorts binary tree by levels by completing BFS."""
    if not node:
        return []
    res = []
    queue = deque([node])
    while queue:
        node = queue.popleft()
        res.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res
