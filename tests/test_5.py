import pytest
from project.task_5.hash_table import HashTable


class TestHashTable:
    """
    Test cases for HashTable class

    """

    def test_unhashable_key(self):
        """'
        Test with unhashable key (should fail)

        """

        table = HashTable()

        with pytest.raises(TypeError):
            table[["Hello"]] = 1

        with pytest.raises(TypeError):
            table[{"name": "Elena"}] = 1

    def test_empty_table(self):
        """
        Operations with empty hash table

        """
        table = HashTable()

        assert len(table) == 0
        assert "key" not in table

        with pytest.raises(KeyError):
            i = table["A"]

        with pytest.raises(KeyError):
            del table["A"]

        assert list(table) == []

    def test_operations(self):
        """
        Insert, get, delete

        """
        table = HashTable()

        table["name"] = "Eva"
        table["age"] = 22

        assert table["name"] == "Eva"
        assert table["age"] == 22
        assert len(table) == 2

        del table["age"]
        assert "age" not in table
        assert len(table) == 1

    def test_collisions(self):
        """
        Collision handling

        """
        table = HashTable(4)

        table[1] = 1
        table[5] = 2

        assert table[1] == 1
        assert table[5] == 2

    def test_resize(self):
        """
        Automatic resizing after adding

        """
        table = HashTable(4)

        for i in range(4):
            table[f"{i}"] = i

        assert table._size == 8

        for i in range(4):
            assert table[f"{i}"] == i

        table["new"] = 10
        assert table["new"] == 10

    def test_wrong_key(self):
        """
        Testing wrong key

        """
        table = HashTable(2)

        with pytest.raises(KeyError):
            t = table["A"]

        with pytest.raises(KeyError):
            del table["A"]

    def test_iteration(self):
        """
        Key iteration

        """
        table = HashTable()
        keys = ["x", "y", "z"]

        for k in keys:
            table[k] = 1

        assert set(iter(table)) == set(keys)

    def test_update_value(self):
        """
        Value update

        """
        table = HashTable()

        table["A"] = 1
        table["A"] = 2

        assert table["A"] == 2
        assert len(table) == 1
