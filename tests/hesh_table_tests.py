import pytest
from collections.abc import MutableMapping
from hash_table import *


class TestHashTable:
    def test_init_data(self):
        """Initial data"""
        data = {"a": 1, "b": 2}
        ht = HashTable(data)
        assert ht["a"] == 1
        assert ht["b"] == 2

    def test_delit_all(self):
        """Test of deliting all item"""
        ht = HashTable({"a": 1, "b": 2, "c": 3})
        for key in ht:
            del ht[key]

        assert "a" not in ht
        assert "b" not in ht
        assert "c" not in ht

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
        """Test of deliting item"""
        ht = HashTable({"a": 1, "b": 2, "c": 3})
        del ht["b"]

        assert "a" in ht
        assert "b" not in ht
        assert "c" in ht
        assert len(ht) == 2

    def test_contains(self):
        """Test contains in table'"""
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
