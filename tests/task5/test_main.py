import pytest
from typing import Any
from project.task5.main import HashTable


class TestHashTable:
    """
    Test class for hash table functionality verification.
    """

    def test_basic_operations(self) -> None:
        """
        Tests basic hash table operations.

        Operations:
            - Element addition
            - Value retrieval
            - Value update
            - Size verification
        """
        ht = HashTable()

        ht["key1"] = "value1"
        ht["key2"] = "value2"

        assert ht["key1"] == "value1"
        assert ht["key2"] == "value2"
        assert len(ht) == 2

        ht["key1"] = "new_value1"
        assert ht["key1"] == "new_value1"
        assert len(ht) == 2

    def test_key_error_on_missing_key(self) -> None:
        """
        Tests KeyError generation when accessing non-existent key.

        Expects:
            KeyError when accessing missing key
        """
        ht = HashTable()

        with pytest.raises(KeyError):
            _ = ht["missing_key"]

    def test_contains_operator(self) -> None:
        """
        Tests in operator for key existence checking.

        Operations:
            - Existing key check
            - Missing key check
        """
        ht = HashTable()
        ht["existing"] = "value"

        assert "existing" in ht
        assert "missing" not in ht

    def test_deletion(self) -> None:
        """
        Tests element deletion operations.

        Operations:
            - Existing element deletion
            - Size verification after deletion
            - Attempt to delete non-existent element
        """
        ht = HashTable()
        ht["key1"] = "value1"
        ht["key2"] = "value2"

        del ht["key1"]

        assert "key1" not in ht
        assert "key2" in ht
        assert len(ht) == 1

        with pytest.raises(KeyError):
            del ht["key1"]

    def test_iteration(self) -> None:
        """
        Tests various table iteration methods.

        Iteration methods:
            - Key iteration
            - Value iteration
            - Key-value pair iteration
        """
        ht = HashTable()
        test_data = {"a": 1, "b": 2, "c": 3}

        for k, v in test_data.items():
            ht[k] = v

        assert set(ht.keys()) == set(test_data.keys())
        assert set(ht.values()) == set(test_data.values())
        assert dict(ht.items()) == test_data
        assert set(iter(ht)) == set(test_data.keys())

    def test_collision_handling(self) -> None:
        """
        Tests collision resolution in hash table.

        Creates:
            Small table to force collisions

        Verifies:
            - Correct element storage despite collisions
            - Access to all elements despite collisions
        """
        ht = HashTable(initial_size=2)

        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3
        ht["d"] = 4

        assert ht["a"] == 1
        assert ht["b"] == 2
        assert ht["c"] == 3
        assert ht["d"] == 4
        assert len(ht) == 4

    def test_resize(self) -> None:
        """
        Tests automatic table resizing.

        Process:
            - Creates table with small capacity
            - Adds elements until resize triggers
            - Verifies capacity increase
            - Verifies data preservation after resize
        """
        ht = HashTable(initial_size=4, load_factor=0.5)

        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        assert ht.capacity > 4
        assert ht["a"] == 1
        assert ht["b"] == 2
        assert ht["c"] == 3
        assert len(ht) == 3

    def test_clear(self) -> None:
        """
        Tests table clearing method.

        Operations:
            - Element addition
            - Table clearing
            - Empty table verification
        """
        ht = HashTable()
        ht["a"] = 1
        ht["b"] = 2

        ht.clear()

        assert len(ht) == 0
        assert "a" not in ht
        assert "b" not in ht

    def test_get_method(self) -> None:
        """
        Tests get method with various parameters.

        Cases:
            - Existing key retrieval
            - Missing key retrieval without default
            - Missing key retrieval with default
        """
        ht = HashTable()
        ht["existing"] = "value"

        assert ht.get("existing") == "value"
        assert ht.get("missing") is None
        assert ht.get("missing", "default") == "default"

    def test_mutable_mapping_interface(self) -> None:
        """
        Tests MutableMapping interface compliance.

        Methods:
            - update
            - pop
            - setdefault
        """
        ht = HashTable()

        ht.update({"x": 10, "y": 20})
        assert ht["x"] == 10
        assert ht["y"] == 20

        value = ht.pop("x")
        assert value == 10
        assert "x" not in ht

        assert ht.pop("missing", "default") == "default"

        assert ht.setdefault("y", 100) == 20
        assert ht.setdefault("z", 30) == 30
        assert ht["z"] == 30

    def test_string_representation(self) -> None:
        """
        Tests table string representation.

        Verifies:
            - Empty table representation
            - Table with elements representation
        """
        ht = HashTable()
        assert str(ht) == "{}"

        ht["a"] = 1
        ht["b"] = 2

        representation = str(ht)
        assert "'a': 1" in representation
        assert "'b': 2" in representation

    def test_initialization_validation(self) -> None:
        """
        Tests initialization parameter validation.

        Cases:
            - Invalid initial_size
            - Invalid load_factor
        """
        with pytest.raises(ValueError):
            HashTable(initial_size=0)

        with pytest.raises(ValueError):
            HashTable(load_factor=0)

        with pytest.raises(ValueError):
            HashTable(load_factor=1.5)

    def test_comprehensive_operations(self) -> None:
        """
        Comprehensive testing of various operations with large element count.

        Process:
            - Adding 100 elements
            - Verifying all elements
            - Removing some elements
            - Verifying remaining elements
        """
        ht = HashTable()

        for i in range(100):
            ht[f"key{i}"] = i

        assert len(ht) == 100

        for i in range(100):
            assert ht[f"key{i}"] == i

        for i in range(0, 100, 2):
            del ht[f"key{i}"]

        assert len(ht) == 50

        for i in range(1, 100, 2):
            assert ht[f"key{i}"] == i

        for i in range(0, 100, 2):
            assert f"key{i}" not in ht


def test_hash_table_with_different_key_types() -> None:
    """
    Tests hash table operation with various key types.

    Key types:
        - Strings
        - Integers
        - Floating point numbers
        - Tuples (if they are hashable)
    """
    ht = HashTable()

    ht["string"] = 1
    ht[123] = "number"
    ht[45.67] = "float"
    ht[(1, 2)] = "tuple"

    assert ht["string"] == 1
    assert ht[123] == "number"
    assert ht[45.67] == "float"
    assert ht[(1, 2)] == "tuple"


def test_hash_table_performance() -> None:
    """
    Tests performance with large number of elements.

    Process:
        - Adding 1000 elements
        - Verifying all elements accessibility
        - Removing all elements
        - Verifying table emptiness
    """
    ht = HashTable()

    for i in range(1000):
        ht[f"key_{i}"] = f"value_{i}"

    for i in range(1000):
        assert ht[f"key_{i}"] == f"value_{i}"

    for i in range(1000):
        del ht[f"key_{i}"]

    assert len(ht) == 0


if __name__ == "__main__":
    """
    Entry point for direct test execution.

    Executes:
        pytest.main: Runs all tests in current file
    """
    pytest.main([__file__])
