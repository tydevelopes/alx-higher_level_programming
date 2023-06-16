"""module defines a test class"""

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        """test instance initialisation"""

        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_init_without_id(self):
        """test instance initialisation"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_nb_objects_increment(self):
        """test object count"""

        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(Base.__nb_objects, 3)  # Private attribute access


if __name__ == "__main__":
    unittest.main()
