from collections.abc import MutableMapping
from typing import Any, List, Tuple, Hashable, Iterator


class HashTable(MutableMapping):
    """
    A hash table implementation using separate chaining for collision resolution
    This class implements a dictionary-like interface that stores key-value pairs
    in a dynamically resizing array of buckets

    Attributes:
        _size: The current capacity of the hash table (number of buckets)
        _count: The current number of key-value pairs
        _buckets: Array of buckets where each
                  bucket contains a list of key-value pairs that hash to that index

    """

    def __init__(self, initial_size: int = 16):
        """
        Initialize the hash table

        Args:
                initial_size: size of the hash table (default: 16)

        Raises:
                ValueError: If initial_size <= 0
        """

        if initial_size <= 0:
            raise ValueError("Initial size must be positive")

        self._size = initial_size
        self._count = 0
        self._buckets: List[List[Tuple[Hashable, Any]]] = [
            [] for _ in range(initial_size)
        ]

    def _hash(self, key: Hashable) -> int:
        """
        Hash function using Python's built-in hash

        Args:
              key: The key to compute hash for (must be hashable)

        Returns:
              int: hash value in range [0, size - 1]

        """
        return hash(key) % self._size

    def _resize(self, new_size: int):
        '''
        Resize the hash table to a new size and rehash all elements

        Args:
              new_size: The new size for the hash table
              """

        '''

        old_buckets = self._buckets
        self._size = new_size
        self._count = 0
        self._buckets = [[] for _ in range(new_size)]

        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value

    def __setitem__(self, key: Hashable, value: Any):
        """
        Set a key-value pair in the hash table
        If the key is already exists, its value if updated

        Args:
              key: The key to set (must be hashable)
              value: The value to associate with the key

        """

        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (old_key, old_value) in enumerate(bucket):
            if old_key == key:
                bucket[i] = (key, value)
                return

        if self._count >= self._size * 0.75:
            self._resize(self._size * 2)
            index = self._hash(key)
            bucket = self._buckets[index]

        bucket.append((key, value))
        self._count += 1

    def __getitem__(self, key: Hashable) -> Any:
        """
        Get the value associated with a key

        Args:
              key: The key to search (must be hashable)

        Returns:
              The value associated with the key

        Raises:
              KeyError: If the key is not found

        """

        index = self._hash(key)
        bucket = self._buckets[index]

        for old_key, value in bucket:
            if old_key == key:
                return value

        raise KeyError("Key is not found")

    def __delitem__(self, key: Hashable):
        """
        Remove a key-value pair

        Args:
              key: The key need to remove (must be hashable)

        Raises:
              KeyError: If the key is not found

        """

        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (old_key, value) in enumerate(bucket):
            if old_key == key:
                del bucket[i]
                self._count -= 1
                return

        raise KeyError("Key is not found")

    def __contains__(self, key: Hashable) -> bool:
        """
        Check if a key exists

        Args:
              key: The key need to check (must be hashable)

        Returns:
              True if the key exists, False otherwise
        """

        index = self._hash(key)
        bucket = self._buckets[index]

        for old_key, value in bucket:
            if old_key == key:
                return True

        return False

    def __iter__(self) -> Iterator[Hashable]:
        """
        Iterate over all keys in the hash table

        Yields:
              Each key in the hash table

        """
        for bucket in self._buckets:
            for key, value in bucket:
                yield key

    def __len__(self) -> int:
        """
        Return the number of pairs in the hash table

        Returns:
                Number of pairs (count)

        """
        return self._count
