import unittest


def curry_explicit(function, arity):
    def curry(*args):
        if len(args) == arity:
            return function(*args)

        def curried(*more_args):
            return curry(*(args + more_args))

        return curried

    return curry


def uncurry_explicit(function, arity):
    def uncurried(*args):
        return function(*args)

    return uncurried


class TestCurryUncurryFunctions(unittest.TestCase):
    def test_curry_function(self):
        curried_add = curry_explicit(lambda x, y: x + y, 2)
        self.assertEqual(curried_add(3)(4), 7)  # Test the curried function

    def test_uncurry_function(self):
        curried_add = curry_explicit(lambda x, y: x + y, 2)
        uncurried_add = uncurry_explicit(curried_add, 2)
        self.assertEqual(uncurried_add(5, 7), 12)  # Test the uncurried function


if __name__ == "__main__":
    unittest.main()
