# Example:
from functools import lru_cache

from src.a_node import Node
from src.b_three_height_of_a_binary_tree import height_of_binary_tree
from src.c_tree_level_order_traversal import level_order_traversal
from src.d_swap_nodes_algorithm import swap_nodes_at_level

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Example: Height of binary tree
print(f"{height_of_binary_tree(root)=}")  # Output: 3

# Example: Level order traversal
print(f"{level_order_traversal(root)=}")  # Output: [[1], [2, 3], [4, 5]]


@lru_cache(maxsize=None)
def was_swapped_msg(swapped: int) -> str:
	return "Swapped" if swapped == 1 else "No swap"


# Example: Swap nodes at level 2
swapped = swap_nodes_at_level(root, 2)
msg = f"level=2, {swapped=}: {level_order_traversal(root)} -> {was_swapped_msg(swapped)}"
print(msg)  # Output: [[1], [2, 3], [5, 4]]

# Example: Swap nodes at level 1
swapped = swap_nodes_at_level(root, 1)
msg = f"level=1, {swapped=}: {level_order_traversal(root)} -> {was_swapped_msg(swapped)}"

print(msg)  # Output: [[1], [3, 2], [4, 5]]

# Example: Swap nodes at level 3
swapped = swap_nodes_at_level(root, 3)
msg = f"level=3, {swapped=}: {level_order_traversal(root)} -> {was_swapped_msg(swapped)}"
print(msg)  # Output: [[1], [3, 2], [4, 5]]

# Example: Swap nodes at level 4
swapped = swap_nodes_at_level(root, 4)
msg = f"level=4, {swapped=}: {level_order_traversal(root)} -> {was_swapped_msg(swapped)}"
print(msg)  # Output: Level 4 does not exist in the tree.
