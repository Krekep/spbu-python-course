import pytest
import random
from project.cartesian_tree import CartesianTree


@pytest.mark.parametrize(
    "key,value",
    [
        (random.randint(1, 100), random.random()),
        (-5, "negative key"),
        (0, "zero"),
        (1, "one"),
        (99999, "large number"),
        (0.123456789, "float key"),
        ("apple", "fruit"),
        ("key", "value"),
    ],
)
def test_insert_and_getitem(key, value):
    """
    Tests that an item can be inserted into the CartesianTree and subsequently retrieved.

    Args:
        key (object): Key to insert in the tree.
        value (object): Value associated with the key.
    """
    tree = CartesianTree()
    tree[key] = value
    assert tree[key] == value


@pytest.mark.parametrize(
    "key,value",
    [
        (random.randint(1, 100), random.random()),
        (random.randint(1, 1000), "random string"),
        (10, "ten"),
        ("another key", 100),
    ],
)
def test_delitem(key, value):
    """
    Tests deletion of an item from the cartesian tree.

    Args:
        key (object): Key to delete from the tree.
        value (object): Value associated with the key before deletion.
    """
    tree = CartesianTree()
    tree[key] = value
    del tree[key]
    with pytest.raises(KeyError):
        tree[key]


@pytest.mark.parametrize(
    "keys",
    [
        [1, 2, 3, 4, 5],
        [10, 100, 1000, 10000, 100000],
        [-3, -1, 0, 2],
    ],
)
def test_inorder_traversal(keys):
    """
    Tests in-order traversal of keys in the cartesian tree.

    Args:
        keys (list[int]): List of keys to insert and verify in sorted order.
    """
    tree = CartesianTree()
    for key in keys:
        tree[key] = key * 2
    sorted_keys = sorted(keys)
    assert list(tree) == sorted_keys


@pytest.mark.parametrize(
    "keys",
    [
        [1, 2, 3, 4, 5],
        [10, 100, 1000, 10000, 100000],
        [-3, -1, 0, 2],
    ],
)
def test_reverse_inorder_traversal(keys):
    """
    Tests reverse in-order traversal of keys in the cartesian tree.

    Args:
        keys (list[int]): List of keys to insert and verify in reverse sorted order.
    """
    tree = CartesianTree()
    for key in keys:
        tree[key] = key * 2
    reversed_keys = sorted(keys, reverse=True)
    assert list(reversed(tree)) == reversed_keys


@pytest.mark.parametrize(
    "key,value",
    [
        (random.randint(1, 100), random.random()),
        (random.randint(1000, 5000), "string value"),
        (-10, "negative value"),
        (0, "zero value"),
    ],
)
def test_contains(key, value):
    """
    Tests the `in` operator for checking the existence of a key in the cartesian tree.

    Args:
        key (object): Key to check existence for in the tree.
        value (object): Value associated with the key.
    """
    tree = CartesianTree()
    tree[key] = value
    assert key in tree
    assert (key + 1) not in tree


@pytest.mark.parametrize(
    "key,value",
    [
        (random.randint(1, 100), random.random()),
        (99999, "large value"),
        ("hello", "world"),
        (-99, "negative number"),
    ],
)
def test_update_existing_item(key, value):
    """
    Tests updating an existing item in the cartesian tree.

    Args:
        key (object): Key of the item to update.
        value (object): New value to update the existing key with.
    """
    tree = CartesianTree()
    tree[key] = value
    new_value = f"updated {value}"
    tree[key] = new_value
    assert tree[key] == new_value


@pytest.mark.parametrize(
    "keys",
    [
        [1, 5, 3, 7, 2],
        [100, 200, 50, 300],
    ],
)
def test_size(keys):
    """
    Tests that the size of the cartesian tree matches the number of inserted keys.

    Args:
        keys (list[int]): List of keys to insert into the tree.
    """
    tree = CartesianTree()
    for key in keys:
        tree[key] = key * 10
    assert len(tree) == len(keys)


@pytest.mark.parametrize(
    "key,value1,value2",
    [
        (random.randint(1, 100), "first value", "second value"),
        (0, "zero1", "zero2"),
        ("apple", "fruit1", "fruit2"),
    ],
)
def test_multiple_insertions_same_key(key, value1, value2):
    """
    Tests multiple insertions with the same key in the cartesian tree, expecting the latest insertion to overwrite.

    Args:
        key (object): Key to insert multiple times with different values.
        value1 (object): Initial value for the key.
        value2 (object): Updated value to replace the initial value.
    """
    tree = CartesianTree()
    tree[key] = value1
    tree[key] = value2
    assert tree[key] == value2
