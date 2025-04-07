import random
from typing import Optional, Iterator, Tuple, Any
from collections.abc import MutableMapping


class TreapNode:
    def __init__(self, key: int, value: Any, priority: Optional[int] = None) -> None:
        """
        Узел структуры данных Treap.

        Attributes:
        key (int): Ключ узла.
        value (Any): Значение, связанное с ключом.
        priority (int): Приоритет узла (случайное значение по умолчанию).
        left (Optional[TreapNode]): Левый дочерний узел.
        right (Optional[TreapNode]): Правый дочерний узел.

        Args:
        key (int): Ключ узла.
        value (Any): Значение узла.
        priority (Optional[int]): Опциональный приоритет узла.

        Returns:
        Нет возвращаемого значения.

        Raises:
        Нет исключений.
        """
        self.key: int = key
        self.value: Any = value
        self.priority: int = (priority if priority is not None else random.randint(1, 2**31 - 1))
        self.left: Optional[TreapNode] = None
        self.right: Optional[TreapNode] = None


class Treap(MutableMapping):
    """
    Реализация структуры данных Treap (дерево + куча), поддерживающей интерфейс MutableMapping.

    Treap сочетает свойства бинарного дерева поиска и кучи, обеспечивая эффективные операции вставки, удаления и поиска.
    """

    def __init__(self, root: Optional[TreapNode] = None) -> None:
        """
        Args:
        root (Optional[TreapNode]): Корневой узел Treap (по умолчанию None).

        Returns:
        Нет возвращаемого значения (конструктор).

        Raises:
        Нет исключений.
        """
        self.root: Optional[TreapNode] = root

    def split(self, node: Optional[TreapNode], key: int) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
        """
        Разделяет Treap на два поддерева по заданному ключу.

        Args:
        node (Optional[TreapNode]): Корневой узел для разделения.
        key (int): Ключ для разделения.

        Returns:
        Tuple[Optional[TreapNode], Optional[TreapNode]]: Два поддерева (ключи < key и ключи >= key).

        Raises:
        Нет исключений.
        """
        if node is None:
            return None, None
        elif key < node.key:
            left, node.left = self.split(node.left, key)
            return left, node
        else:
            node.right, right = self.split(node.right, key)
            return node, right

    def merge(self, left_node: Optional[TreapNode], right_node: Optional[TreapNode]) -> Optional[TreapNode]:
        """
        Объединяет два Treap в один с сохранением свойств структуры.

        Args:
        left_node (Optional[TreapNode]): Корень левого поддерева.
        right_node (Optional[TreapNode]): Корень правого поддерева.

        Returns:
        Optional[TreapNode]: Корень объединенного дерева.

        Raises:
        Нет исключений.
        """
        if right_node is None:
            return left_node
        if left_node is None:
            return right_node
        elif left_node.priority > right_node.priority:
            left_node.right = self.merge(left_node.right, right_node)
            return left_node
        else:
            right_node.left = self.merge(left_node, right_node.left)
            return right_node



    def insert(self, node: TreapNode, key: int, value: Any) -> TreapNode:
        """
        Вставляет новый узел или обновляет значение существующего.

        Args:
        node (TreapNode): Корневой узел.
        key (int): Ключ для вставки.
        value (Any): Значение для вставки.

        Returns:
        TreapNode: Корень дерева после вставки.

        Raises:
        Нет исключений.
        """
        new_node = self.get_node(key)
        if new_node is not None:
            new_node.value = value
            return self.root
        
        new_node = TreapNode(key, value)
        node_1, node_2 = self.split(node, key)
        return self.merge(self.merge(node_1, new_node), node_2)



    def __len__(self) -> int:
        """
        Возвращает узел по ключу.

        Args:
        key (int): Ключ для поиска.

        Returns:
        TreapNode: Найденный узел или None.

        Raises:
        Нет исключений.
        """
        return sum(1 for _ in self)

    def __contains__(self, key: Any) -> bool:
        """
        Итератор для обхода Treap в порядке возрастания ключей.

        Args:
        node (Optional[TreapNode]): Корневой узел для обхода.

        Yields:
        Iterator: Ключи дерева в порядке возрастания.

        Raises:
        Нет исключений.
        """
        try:
            self[key] 
            return True
        except KeyError:
            return False

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Итератор для обхода Treap в порядке убывания ключей.

        Args:
        node (Optional[TreapNode]): Корневой узел для обхода.

        Yields:
        Iterator: Ключи дерева в порядке убывания.

        Raises:
        Нет исключений.
        """
        self.root = self.insert(self.root, key, value)

    

    def get_node(self, key: int) -> TreapNode:
        """
        Поиск узла в Treap по заданному ключу.

        Args:
        key (int): Ключ для поиска в дереве.

        Returns:
        TreapNode: Найденный узел или None, если узел с таким ключом не существует.

        Raises:
        Нет исключений.
        """
        node = self.root
        while node:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    
    def __getitem__(self, key: int) -> str:
        """
        Возвращает значение по ключу.

        Args:
        key (int): Ключ для поиска.

        Returns:
        str: Значение, связанное с ключом.

        Raises:
        KeyError: Если ключ не найден.
        """
        node = self.get_node(key)
        if node == None:
            raise KeyError(f"Key {key} not found.")
        return node.value



    def __delitem__(self, key: int) -> None:
        """
        Удаляет узел с указанным ключом.

        Args:
        key (int): Ключ для удаления.

        Returns:
        Нет возвращаемого значения.

        Raises:
        KeyError: Если ключ не найден.
        """
        parent = None
        node = self.root

        while node and node.key != key:
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if node is None:
            raise KeyError(f"Key {key} not found")

        new_child = self.merge(node.left, node.right)

        if parent is None:
            self.root = new_child
        elif parent.left == node:
            parent.left = new_child
        else:
            parent.right = new_child

            

    def __iter__(self) -> Iterator:
        """
        Возвращает итератор для обхода ключей в порядке возрастания.

        Args:
        Нет аргументов.

        Returns:
        Iterator: Итератор по ключам.

        Raises:
        Нет исключений.
        """
        return self.inorder_iter(self.root)

    def inorder_iter(self, node: Optional[TreapNode]) -> Iterator:
        """
        Вспомогательный метод для inorder-обхода (по возрастанию).

        Args:
        node (Optional[TreapNode]): Узел для начала обхода.

        Yields:
        Iterator: Ключи в порядке возрастания.

        Raises:
        Нет исключений.
        """
        if node:
            yield from self.inorder_iter(node.left)
            yield node.key
            yield from self.inorder_iter(node.right)

    def __reversed__(self) -> Iterator:
        """
        Возвращает итератор для обхода ключей в порядке убывания.

        Args:
        Нет аргументов.

        Returns:
        Iterator: Итератор по ключам.

        Raises:
        Нет исключений.
        """
        return self.reverse_inorder_iter(self.root)

    def reverse_inorder_iter(self, node: Optional[TreapNode]) -> Iterator:
        """
        Вспомогательный метод для обратного inorder-обхода (по убыванию).

        Args:
        node (Optional[TreapNode]): Узел для начала обхода.

        Yields:
        Iterator: Ключи в порядке убывания.

        Raises:
        Нет исключений.
        """
        if node:
            yield from self.reverse_inorder_iter(node.right)
            yield node.key
            yield from self.reverse_inorder_iter(node.left)

    def __repr__(self) -> str:
        """
        Returns the string representation of the Treap.

        Returns
        -------
        str
            The string representation of the Treap.
        """
        return f"Treap({list(self)})"




# if __name__ == "__main__":
#     treap = Treap()

#     treap["d"] = 4
#     treap["b"] = 2
#     treap["f"] = 6
#     left, right = treap.split(treap.root, "b")

#     merged_tree = Treap(treap.merge(left, right))

#     print(list(merged_tree)) #== ["b", "d", "f"]
#     print(len(merged_tree))
#     print(merged_tree["b"])
#     del merged_tree["b"]
#     print(list(merged_tree))
#     merged_tree["b"] = 5
#     print(list(merged_tree))
#     print(merged_tree["b"])
#     merged_tree["b"] = 10
#     print(merged_tree["b"])
#     print(list(merged_tree)) 