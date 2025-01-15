

from typing import Self


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Self = None
        self.right: Self = None