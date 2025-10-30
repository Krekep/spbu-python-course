import pytest
from collections.abc import MutableMapping
from project.hash_table import HashTable


class TestHashTable:
    def test_init_data(self):
        """Initial data"""
        data = {"a": 1, "b": 2}
        ht = HashTable(data)
        assert ht["a"] == 1
        assert ht["b"] == 2

    def test_delit_all(self):
        """Test of deleting all items"""
        ht = HashTable({"a": 1, "b": 2, "c": 3})

        keys = list(ht)
        for key in keys:
            del ht[key]

        assert "a" not in ht
        assert "b" not in ht
        assert "c" not in ht
        assert len(ht) == 0

    def test_set(self):
        """Testing set the element"""
        ht = HashTable()
        ht["key1"] = "value1"
        ht["key2"] = "value2"

        assert ht["key1"] == "value1"
        assert ht["key2"] == "value2"
        assert len(ht) == 2

    def test_update(self):
        """Test of updating existed elements"""
        ht = HashTable({"a": 1})
        ht["a"] = 100
        assert ht["a"] == 100
        assert len(ht) == 1

    def test_delit(self):
        """Test of deleting item"""
        ht = HashTable({"a": 1, "b": 2, "c": 3})
        del ht["b"]

        assert "a" in ht
        assert "b" not in ht
        assert "c" in ht
        assert len(ht) == 2

    def test_contains(self):
        """Test contains in table"""
        ht = HashTable({"a": 1, "b": 2})
        assert "a" in ht
        assert "b" in ht
        assert "c" not in ht

    def test_len(self):
        """Test of len of the table"""
        ht = HashTable()
        assert len(ht) == 0

        ht["a"] = 1
        assert len(ht) == 1

        ht["b"] = 2
        assert len(ht) == 2

    def test_iter(self):
        """Test of iteration"""
        data = {"a": 1, "b": 2, "c": 3}
        ht = HashTable(data)
        keys = list(ht)

        assert set(keys) == {"a", "b", "c"}
        assert len(keys) == 3

    def test_collisions(self):
        """Test collision handling"""
        ht = HashTable()

        for i in range(100):
            ht[f"key{i}"] = f"value{i}"

        for i in range(100):
            assert ht[f"key{i}"] == f"value{i}"

        assert len(ht) == 100

    def test_delete_nonexistent(self):
        """Test deleting non-existent key"""
        ht = HashTable({"a": 1})
        with pytest.raises(KeyError):
            del ht["nonexistent"]

    def test_get_nonexistent(self):
        """Test getting non-existent key"""
        ht = HashTable({"a": 1})
        with pytest.raises(KeyError):
            _ = ht["nonexistent"]

    def test_empty_iteration(self):
        """Test iteration over empty table"""
        ht = HashTable()
        keys = list(ht)
        assert len(keys) == 0

    def test_reinsert_after_delete(self):
        """Test reinserting key after deletion"""
        ht = HashTable()
        ht["key"] = "value1"
        del ht["key"]
        ht["key"] = "value2"

        assert ht["key"] == "value2"
        assert len(ht) == 1

    def test_multiple_updates(self):
        """Test multiple updates to same key"""
        ht = HashTable()
        ht["key"] = "value1"
        ht["key"] = "value2"
        ht["key"] = "value3"

        assert ht["key"] == "value3"
        assert len(ht) == 1
