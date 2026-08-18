import unittest

from greeting import greet


class GreetingTest(unittest.TestCase):
    def test_non_blank_name_is_trimmed(self):
        self.assertEqual("Hello, Ada!", greet("  Ada  "))


if __name__ == "__main__":
    unittest.main()
