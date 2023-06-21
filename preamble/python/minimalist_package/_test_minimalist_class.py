"""
The 'unittest' package is built-in. Always rely on it first as it will be available
in every platform, always, and supported with the other default Python packages.
https://docs.python.org/3.10/library/unittest.html
"""
import unittest
from . import MinimalistClass


class TestMinimalistClass(unittest.TestCase):
    """For each `TestCase`, we create a subclass of `unittest.TestCase`."""

    def setUp(self):
        self.minimalist_instance = MinimalistClass(attribute_arg=15.0,
                                                   private_attribute_arg=35.0)

    def test_attribute(self):
        self.assertEqual(self.minimalist_instance.attribute, 15.0)

    def test_private_attribute(self):
        self.assertEqual(self.minimalist_instance._private_attribute, 35.0)

    def test_method(self):
        self.assertEqual(self.minimalist_instance.method(), 15.0 + 35.0)

    def test_get_set_private_attribute(self):
        self.minimalist_instance.set_private_attribute(20.0)
        self.assertEqual(self.minimalist_instance.get_private_attribute(), 20.0)
        # Reset the value to what we expect for the other tests
        self.minimalist_instance.set_private_attribute(35.0)

    def test_static_method(self):
        self.assertEqual(MinimalistClass.static_method(), "Hello World!")


def main():
    unittest.main()