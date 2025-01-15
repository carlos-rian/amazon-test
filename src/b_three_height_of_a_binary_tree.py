from functools import lru_cache

from src.a_node import Node


@lru_cache(maxsize=None)
def height_of_binary_tree(root: Node) -> int:
    if not root:
        return -1  # Use 0 if counting nodes instead of edges

    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)

    return max(left_height, right_height) + 1
