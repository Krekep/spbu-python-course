from collections.abc import MutableMapping
import random


class Node:
    """
    The class 'Node' represents a node in a Cartesian tree
    Attributes:
            key (any type): The node key used for searching and sorting.
            priority (int): Random priority used for balancing the tree.
            value (any type): An additional value associated with the key.
            left (Node): The left child node.
            right (Node): The right child node.
    """

    def __init__(self, key, priority, value=None):
        self.key = key
        self.priority = priority
        self.value = value
        self.left = None
        self.right = None
