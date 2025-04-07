from project.Treap.treap import Treap
import pytest


def test_insert_and_get():
    treap = Treap()

    treap["a"] = 10
    treap["b"] = 20
    treap["c"] = 30

    assert treap["a"] == 10
    assert treap["b"] == 20
    assert treap["c"] == 30


def test_update_existing_key():
    treap = Treap()

    treap["a"] = 10
    treap["a"] = 100

    assert treap["a"] == 100


def test_key_existence():
    treap = Treap()

    treap["x"] = 5
    treap["y"] = 15

    assert "x" in treap
    assert "y" in treap
    assert "z" not in treap


def test_delete_key():
    treap = Treap()

    treap["key"] = 123
    del treap["key"]

    assert "key" not in treap

    with pytest.raises(KeyError):
        del treap["nonexistent_key"]


def test_inorder_traversal():
    treap = Treap()

    treap["m"] = 1
    treap["c"] = 2
    treap["z"] = 3

    keys_in_order = list(treap)
    assert keys_in_order == ["c", "m", "z"]


def test_reverse_inorder_traversal():
    treap = Treap()

    treap["b"] = 20
    treap["a"] = 10
    treap["c"] = 30

    reversed_keys = list(reversed(treap))
    assert reversed_keys == ["c", "b", "a"]


def test_split():
    treap = Treap()

    treap["d"] = 4
    treap["b"] = 2
    treap["f"] = 6
    treap["a"] = 1
    treap["c"] = 3
    treap["e"] = 5

    left, right = treap.split(treap.root, "c")

    assert list(treap.inorder_iter(left)) == ["a", "b", "c"]
    assert list(treap.inorder_iter(right)) == ["d", "e", "f"]


def test_merge():
    treap = Treap()

    left = Treap()
    right = Treap()

    left["a"] = 1
    left["b"] = 2
    right["c"] = 3
    right["d"] = 4

    merged_tree = treap.merge(left.root, right.root)
    assert list(treap.inorder_iter(merged_tree)) == ["a", "b", "c", "d"]


def test_insert_with_split_and_merge():
    treap = Treap()

    treap["d"] = 4
    treap["b"] = 2
    treap["f"] = 6
    left, right = treap.split(treap.root, "b")

    merged_tree = treap.merge(left, right)
    assert list(treap.inorder_iter(merged_tree)) == ["b", "d", "f"]


def test_large_scale_operations():
    treap = Treap()

    for i in range(1000):
        treap[i] = i * 2

    for i in range(1000):
        assert treap[i] == i * 2
    assert list(treap) == list(range(1000))

    for i in range(1000):
        del treap[i]
    assert len(list(treap)) == 0


def test_iteration_on_empty_treap():
    treap = Treap()
    assert list(treap) == []
    assert list(reversed(treap)) == []


def test_invalid_key_access():
    treap = Treap()

    with pytest.raises(KeyError):
        _ = treap["nonexistent"]