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

    def __setitem__(self, key, value):
        """
        Inserts a new node with the specified key and value
        """
        self.root = self._insert(self.root, key, value)

    def __delitem__(self, key):
        """
        Deletes the node with the specified key.
        """
        self.root = self._delete(self.root, key)

    def insert(self, key, value=None):
        """
        Inserts a new node with the specified key and value.
        """
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        """
        An auxiliary function for recursively inserting a node.
        """
        if node is None:
            return Node(key, random.randint(0, 100000), value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        if node.priority < node.left.priority if node.left else float("inf"):
            node = self.rotate_right(node)
        elif node.priority < node.left.priority if node.right else float("inf"):
            node = self.rotate_left(node)
        return node

    def delete(self, node, key):
        """
        Deletes the node with the specified key.
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """
        An auxiliary function for recursively deleting a node.
        """
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node = self.rotate_left(node)
                node.left = self._delete(node.left, key)
        return node

    def find(self, key):
        """
        Searches for a node with the specified key.
        """
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def rotate_right(self, node):
        """
        Performs a right turn around the specified node.
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def rotate_left(self, node):
        """
        Performs a left turn around the specified node.
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
