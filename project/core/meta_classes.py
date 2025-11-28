class Cell_metaclass(type):
    def __new__(mcs, name, bases, namespace) -> type:
        original_init = namespace.get("__init__")

        def new_init(self, *args: iter, **kwargs: dict) -> None:
            self._x = None
            self._y = None
            self._is_alive = True

            if original_init:
                original_init(self, *args, **kwargs)

        namespace["__init__"] = new_init

        return super().__new__(mcs, name, bases, namespace)
