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


class Treap(MutableMapping):
    """
    The 'Treap' class implements a Cartesian tree,
    which is a self-balancing binary search tree.

    This tree uses node priorities to maintain balance.
    Priorities are randomly generated.

    Tracks can be used to implement dictionaries, sets,
    as well as for other tasks
    where efficient sorting and searching are needed.

     Attributes:
            root (Node): The root node of the tree.
    """

    def __init__(self):
        self.root = None

    def __len__(self):
        """
        returns the number of nodes in the tree
        """
        return self._size(self.root)

    def _size(self, node):
        """
        a function for counting nodes in a subtree
        """
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def __contains__(self, key):
        """
        checks if there is a node with the specified key
        """
        return self.find(key) is not None

    def __getitem__(self, key):
        """
        The function returns the value associated with the specified key
        """
        node = self.find(key)
        if node is None:
            raise KeyError(key)
        return node.value
