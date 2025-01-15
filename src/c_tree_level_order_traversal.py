from collections import deque

from src.a_node import Node


def level_order_traversal(root: Node):
	if not root:
		return []

	queue = deque([root])
	result = []

	while queue:
		level = []
		for _ in range(len(queue)):
			node = queue.popleft()
			level.append(node.value)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		result.append(level)

	return result
