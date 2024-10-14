import unittest


def sample_decorator(func):
    def wrapper(*args, **kwargs):
        return f"Decorated: {func(*args, **kwargs)}"

    return wrapper


def decorate(func):
    return sample_decorator(func)


class TestDecorateFunction(unittest.TestCase):
    def test_decorate_function_behavior(self):
        @decorate
        def greet(name):
            return f"Hello, {name}!"

        result = greet("World")
        self.assertEqual(
            result, "Decorated: Hello, World!"
        )  # Check if the decorator modifies the behavior correctly

    def test_decorate_with_no_arguments(self):
        @decorate
        def no_arg_function():
            return "No arguments"

        result = no_arg_function()
        self.assertEqual(
            result, "Decorated: No arguments"
        )  # Ensure it handles functions with no arguments


if __name__ == "__main__":
    unittest.main()
