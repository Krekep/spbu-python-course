from typing import Any, Iterator, List, Tuple
from collections.abc import MutableMapping, ItemsView, KeysView, ValuesView


class HashTable(MutableMapping):
    """
    Hash table implementation with separate chaining collision resolution.

    Attributes:
        _size : int (Current number of elements in the table)
        _capacity : int (Current table capacity - number of buckets)
        _load_factor : float (Load factor for automatic resizing)
        _buckets : List[List[Tuple[Any, Any]]] (List of buckets, each containing key-value pairs)
    """

    def __init__(self, initial_size: int = 8, load_factor: float = 0.75) -> None:
        """
        Initializes the hash table with given parameters.

        Parameters:
            initial_size : int (Initial table size, must be >= 1)
            load_factor : float (Load factor, must be in range (0, 1])

        Raises:
            ValueError: If initial_size < 1 or load_factor not in range (0, 1]
        """
        if initial_size < 1:
            raise ValueError("Initial size must be at least 1")
        if not 0 < load_factor <= 1:
            raise ValueError("Load factor must be between 0 and 1")

        self._size = 0
        self._capacity = initial_size
        self._load_factor = load_factor
        self._buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(initial_size)]

    def _hash(self, key: Any) -> int:
        """
        Calculates bucket index for the given key.

        Parameters:
            key : Any (Key to hash)

        Returns:
            int: Bucket index in range [0, capacity - 1]
        """
        return hash(key) % self._capacity

    def _should_resize(self) -> bool:
        """
        Checks if table needs to be resized up.

        Returns:
            bool: True if current load factor exceeds threshold, False otherwise
        """
        return self._size / self._capacity > self._load_factor

    def _should_shrink(self) -> bool:
        """
        Checks if table needs to be resized down.

        Returns:
            bool: True if table can be shrunk for memory optimization, False otherwise
        """
        return (
            self._capacity > 8
            and self._size > 0
            and self._size / self._capacity < self._load_factor / 4
        )

    def _resize(self, new_capacity: int) -> None:
        """
        Resizes the hash table and redistributes all elements.

        Parameters:
            new_capacity : int (New table capacity)

        Process:
            - Creates new buckets
            - Rehashes and redistributes all existing elements
            - Maintains element order within chains
        """
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(new_capacity)]
        self._capacity = new_capacity
        self._size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self._set_item_without_resize_check(key, value)

    def _set_item_without_resize_check(self, key: Any, value: Any) -> None:
        """
        Internal method to set value without resize check.

        Parameters:
            key : Any (Key to set)
            value : Any (Value to set)

        Note:
            Used only during resizing to avoid recursion
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Sets value for the given key.

        Parameters:
            key : Any (Key to set value for)
            value : Any (Value to set)

        Process:
            - If key exists, updates value
            - If key doesn't exist, adds new pair
            - Checks for resize after addition
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        key_exists = False
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                key_exists = True
                break

        if not key_exists:
            bucket.append((key, value))
            self._size += 1

            if self._should_resize():
                self._resize(self._capacity * 2)

    def __getitem__(self, key: Any) -> Any:
        """
        Returns value for the given key.

        Parameters:
            key : Any (Key to search for)

        Returns:
            Any: Value associated with the key

        Raises:
            KeyError: If key is not found in the table
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key {key!r} not found")

    def __delitem__(self, key: Any) -> None:
        """
        Removes key and associated value from the table.

        Parameters:
            key : Any (Key to remove)

        Raises:
            KeyError: If key is not found in the table

        Process:
            - Removes key from appropriate bucket
            - Checks if table needs to be shrunk
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1

                if self._should_shrink():
                    self._resize(max(8, self._capacity // 2))
                return

        raise KeyError(f"Key {key!r} not found")

    def __contains__(self, key: Any) -> bool:
        """
        Checks if key exists in the table.

        Parameters:
            key : Any (Key to check)

        Returns:
            bool: True if key is present in table, False otherwise
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    def __len__(self) -> int:
        """
        Returns number of elements in the table.

        Returns:
            int: Current number of elements
        """
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """
        Returns iterator over all keys in the table.

        Returns:
            Iterator[Any]: Iterator yielding keys in bucket traversal order
        """
        for bucket in self._buckets:
            for key, value in bucket:
                yield key

    def keys(self) -> KeysView[Any]:
        """
        Returns view object for table keys.

        Returns:
            KeysView[Any]: View object supporting set operations
        """
        return _HashTableKeysView(self)

    def values(self) -> ValuesView[Any]:
        """
        Returns view object for table values.

        Returns:
            ValuesView[Any]: View object for iterating over values
        """
        return _HashTableValuesView(self)

    def items(self) -> ItemsView[Any, Any]:
        """
        Returns view object for key-value pairs.

        Returns:
            ItemsView[Any, Any]: View object for iterating over key-value pairs
        """
        return _HashTableItemsView(self)

    def get(self, key: Any, default: Any = None) -> Any:
        """
        Returns value for key or default value if key not found.

        Parameters:
            key : Any (Key to search for)
            default : Any (Default value to return if key not found)

        Returns:
            Any: Key value or default if key doesn't exist
        """
        try:
            return self[key]
        except KeyError:
            return default

    def clear(self) -> None:
        """
        Clears the table by removing all elements.

        Process:
            - Resets size to 0
            - Clears all buckets
            - Maintains current table capacity
        """
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    def setdefault(self, key: Any, default: Any = None) -> Any:
        """
        Returns key value if key in table, else sets default.

        Parameters:
            key : Any (Key to search for or set)
            default : Any (Default value to set if key not found)

        Returns:
            Any: Existing key value or default if key was set
        """
        if key in self:
            return self[key]
        else:
            self[key] = default
            return default

    def pop(self, key: Any, default: Any = None) -> Any:
        """
        Removes key and returns its value.

        Parameters:
            key : Any (Key to remove)
            default : Any (Default value if key not found)

        Returns:
            Any: Value of removed key or default

        Raises:
            KeyError: If key not found and default not specified
        """
        if key in self:
            value = self[key]
            del self[key]
            return value
        elif default is not None:
            return default
        else:
            raise KeyError(f"Key {key!r} not found")

    def popitem(self) -> Tuple[Any, Any]:
        """
        Removes and returns arbitrary key-value pair.

        Returns:
            Tuple[Any, Any]: Removed (key, value) pair

        Raises:
            KeyError: If table is empty
        """
        if self._size == 0:
            raise KeyError("popitem(): hash table is empty")

        for bucket in self._buckets:
            if bucket:
                key, value = bucket.pop()
                self._size -= 1
                return key, value

        raise KeyError("popitem(): hash table is empty")

    def __str__(self) -> str:
        """
        Returns string representation of the table.

        Returns:
            str: String in Python dictionary format
        """
        items = []
        for key, value in self.items():
            items.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(items) + "}"

    def __repr__(self) -> str:
        """
        Returns formal string representation of the object.

        Returns:
            str: String that can be used to recreate the object
        """
        return f"HashTable({str(self)})"

    @property
    def load_factor(self) -> float:
        """
        Returns current table load factor.

        Returns:
            float: Ratio of size to capacity
        """
        return self._size / self._capacity

    @property
    def capacity(self) -> int:
        """
        Returns current table capacity.

        Returns:
            int: Number of buckets in the table
        """
        return self._capacity


class _HashTableKeysView(KeysView):
    """
    View object for hash table keys.

    Attributes:
        _table : HashTable (Reference to parent hash table)
    """

    def __init__(self, table: HashTable) -> None:
        """
        Initializes keys view object.

        Parameters:
            table : HashTable (Parent hash table)
        """
        self._table = table

    def __iter__(self) -> Iterator[Any]:
        """
        Returns iterator over table keys.

        Returns:
            Iterator[Any]: Iterator over all keys in the table
        """
        return iter(self._table)

    def __len__(self) -> int:
        """
        Returns number of keys in view.

        Returns:
            int: Number of keys in the table
        """
        return len(self._table)

    def __contains__(self, key: Any) -> bool:
        """
        Checks if key exists in view.

        Parameters:
            key : Any (Key to check)

        Returns:
            bool: True if key is present in table, False otherwise
        """
        return key in self._table


class _HashTableValuesView(ValuesView):
    """
    View object for hash table values.

    Attributes:
        _table : HashTable (Reference to parent hash table)
    """

    def __init__(self, table: HashTable) -> None:
        """
        Initializes values view object.

        Parameters:
            table : HashTable (Parent hash table)
        """
        self._table = table

    def __iter__(self) -> Iterator[Any]:
        """
        Returns iterator over table values.

        Returns:
            Iterator[Any]: Iterator over all values in the table
        """
        for bucket in self._table._buckets:
            for key, value in bucket:
                yield value

    def __len__(self) -> int:
        """
        Returns number of values in view.

        Returns:
            int: Number of values in the table
        """
        return len(self._table)


class _HashTableItemsView(ItemsView):
    """
    View object for hash table key-value pairs.

    Attributes:
        _table : HashTable (Reference to parent hash table)
    """

    def __init__(self, table: HashTable) -> None:
        """
        Initializes items view object.

        Parameters:
            table : HashTable (Parent hash table)
        """
        self._table = table

    def __iter__(self) -> Iterator[Tuple[Any, Any]]:
        """
        Returns iterator over key-value pairs.

        Returns:
            Iterator[Tuple[Any, Any]]: Iterator over all key-value pairs
        """
        for bucket in self._table._buckets:
            for key, value in bucket:
                yield key, value

    def __len__(self) -> int:
        """
        Returns number of pairs in view.

        Returns:
            int: Number of key-value pairs in the table
        """
        return len(self._table)

    def __contains__(self, item: Any) -> bool:
        """
        Checks if key-value pair exists in view.

        Parameters:
            item : Any ((key, value) pair to check)

        Returns:
            bool: True if pair is present in table, False otherwise
        """
        key, value = item
        try:
            v = self._table[key]
            return v == value
        except KeyError:
            return False
