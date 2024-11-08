from collections.abc import MutableMapping
from typing import Optional, Iterator, Tuple, Any
import random


class CartesianTree(MutableMapping):
    """A cartesian tree data structure.
    Allows access, insertion, deletion, and iteration over elements.

    Attributes:
        _root (Optional[_Node]): The root node of the cartesian tree.
        _size (int): The number of nodes in the cartesian tree.
    """

    class _Node:
        """Internal class representing a node in the cartesian tree.

        Attributes:
            key (Any): The key associated with the node.
            value (Any): The value stored in the node.
            priority (int): The priority of the node.
            left (Optional[_Node]): The left child of the node.
            right (Optional[_Node]): The right child of the node.
        """

        def __init__(self, key: Any, value: Any, priority: int):
            self.key = key
            self.value = value
            self.priority = priority
            self.left: Optional[CartesianTree._Node] = None
            self.right: Optional[CartesianTree._Node] = None

    def __init__(self):
        """Initialize an empty cartesian tree."""
        self._root = None
        self._size = 0

    def _insert(
        self, node: Optional[_Node], key: Any, value: Any, priority: int
    ) -> Optional[_Node]:
        """Insert a new element using split and merge.

        Args:
            node (Optional[_Node]): The current node being checked for insertion.
            key (Any): The key to insert.
            value (Any): The value associated with the key.
            priority (int): The priority for balancing the tree.

        Returns:
            Optional[_Node]: The new root of the tree after insertion.
        """
        t1, t2 = self.split(node, key)
        new_node = self._Node(key, value, priority)
        t1 = self.merge(t1, new_node)
        return self.merge(t1, t2)

    def split(
        self, t: Optional[_Node], key: Any
    ) -> Tuple[Optional[_Node], Optional[_Node]]:
        """Split the tree into two subtrees based on the key.

        Args:
            t (Optional[_Node]): The tree to split.
            key (Any): The key to split the tree by.

        Returns:
            Tuple[Optional[_Node], Optional[_Node]]: The two subtrees.
        """
        if t is None:
            return None, None

        if key < t.key:
            t1, t2 = self.split(t.left, key)
            t.left = t2
            return t1, t
        else:
            t1, t2 = self.split(t.right, key)
            t.right = t1
            return t, t2

    def merge(self, t1: Optional[_Node], t2: Optional[_Node]) -> Optional[_Node]:
        """Merge two trees into one.

        Args:
            t1 (Optional[_Node]): The first tree.
            t2 (Optional[_Node]): The second tree.

        Returns:
            Optional[_Node]: The merged tree.
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        if t1.priority > t2.priority:
            t1.right = self.merge(t1.right, t2)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            return t2

    def __setitem__(self, key: Any, value: Any) -> None:
        """Insert a key-value pair into the tree or update an existing key.

        Args:
            key (Any): The key to insert or update.
            value (Any): The value associated with the key.
        """
        node = self._get_node(self._root, key)

        if node:
            node.value = value
        else:
            priority = random.randint(0, 100)
            self._root = self._insert(self._root, key, value, priority)
            self._size += 1

    def __getitem__(self, key: Any) -> Any:
        """Retrieve the value associated with the given key.

        Args:
            key (Any): The key to search for.

        Returns:
            Any: The value associated with the key.

        Raises:
            KeyError: If the key is not found in the tree.
        """
        node = self._get_node(self._root, key)
        if node is None:
            raise KeyError(f"Key '{key}' not found in the tree.")
        return node.value

    def _get_node(self, node: Optional[_Node], key: Any) -> Optional[_Node]:
        """Recursively search for a node by key.

        Args:
            node (Optional[_Node]): The current node being checked.
            key (Any): The key to search for.

        Returns:
            Optional[_Node]: The node with the specified key, if found.
        """
        if node is None:
            return None
        if key < node.key:
            return self._get_node(node.left, key)
        elif key > node.key:
            return self._get_node(node.right, key)
        else:
            return node

    def __delitem__(self, key: Any) -> None:
        """Remove a key-value pair from the tree.

        Args:
            key (Any): The key to remove.

        Raises:
            KeyError: If the key is not found in the tree.
        """
        t1, t2 = self.split(self._root, key)
        if t1 is None:
            raise KeyError(f"Key '{key}' not found in the tree.")

        t1 = self.remove_node(t1, key)
        self._root = self.merge(t1, t2)
        self._size -= 1

    def remove_node(self, t: Optional[_Node], key: Any) -> Optional[_Node]:
        """Remove the node by key from the tree.

        Args:
            t (Optional[_Node]): The subtree to remove the node from.
            key (Any): The key to remove.

        Returns:
            Optional[_Node]: The updated subtree.
        """
        if t is None:
            return None

        if key < t.key:
            t.left = self.remove_node(t.left, key)
        elif key > t.key:
            t.right = self.remove_node(t.right, key)
        else:
            if t.left is None:
                return t.right
            elif t.right is None:
                return t.left
            if t.left is not None and t.right is not None:
                if t.left.priority > t.right.priority:
                    t = self._rotate_right(t)
                    t.right = self.remove_node(t.right, key)  # type: ignore
                else:
                    t = self._rotate_left(t)
                    t.left = self.remove_node(t.left, key)  # type: ignore

        return t

    def _rotate_right(self, node: Optional[_Node]) -> Optional[_Node]:
        """Perform a right rotation around the given node.

        Args:
            node (Optional[_Node]): The node to rotate.

        Returns:
            Optional[_Node]: The new root of the rotated subtree.
        """
        if node is None or node.left is None:
            return node

        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def _rotate_left(self, node: Optional[_Node]) -> Optional[_Node]:
        """Perform a left rotation around the given node.

        Args:
            node (Optional[_Node]): The node to rotate.

        Returns:
            Optional[_Node]: The new root of the rotated subtree.
        """
        if node is None or node.right is None:
            return node

        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def __iter__(self) -> Iterator[Any]:
        """Return an iterator over the keys of the tree in ascending order."""
        yield from self._inorder_traversal(self._root)

    def _inorder_traversal(self, node: Optional[_Node]) -> Iterator[Any]:
        """Perform an in-order traversal to retrieve keys in sorted order.

        Args:
            node (Optional[_Node]): The current node in traversal.

        Yields:
            Any: The next key in ascending order.
        """
        if node:
            yield from self._inorder_traversal(node.left)
            yield node.key
            yield from self._inorder_traversal(node.right)

    def __reversed__(self) -> Iterator[Any]:
        """Return an iterator over the keys of the tree in descending order."""
        yield from self._reverse_inorder_traversal(self._root)

    def _reverse_inorder_traversal(self, node: Optional[_Node]) -> Iterator[Any]:
        """Perform a reverse in-order traversal to retrieve keys in reverse order.

        Args:
            node (Optional[_Node]): The current node in traversal.

        Yields:
            Any: The next key in descending order.
        """
        if node:
            yield from self._reverse_inorder_traversal(node.right)
            yield node.key
            yield from self._reverse_inorder_traversal(node.left)

    def __len__(self) -> int:
        """Return the number of items in the tree."""
        return self._size

    def __contains__(self, key: Any) -> bool:
        """Check if the tree contains the given key.

        Args:
            key (Any): The key to check.

        Returns:
            bool: True if the key exists, otherwise False.
        """
        return self._get_node(self._root, key) is not None
