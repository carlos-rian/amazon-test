from collections import deque
from functools import lru_cache

from src.a_node import Node


def swap_nodes_at_level(root: Node, k: int):
	swapped = 0  # Flag to indicate if any swap was performed
	if not root or k <= 0:
		return swapped

	queue = deque([(root, 1)])  # Pair: (node, level)

	while queue:
		node, level = queue.popleft()

		# If we've reached the desired level
		if level == k:
			node.left, node.right = node.right, node.left
			swapped = 1

		# Add children to queue with their levels
		if node.left:
			queue.append((node.left, level + 1))
		if node.right:
			queue.append((node.right, level + 1))

	return swapped
