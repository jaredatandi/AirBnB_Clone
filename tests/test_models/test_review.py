#!/usr/bin/python3
"""
Unitesting for review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """setting up test cases"""
        self.Joe = Review()
        self.Joe.place_id = "SF"
        self.Joe.user_id = "Decent"
        self.Joe.text = "Cloud"

    def test_id(self):
        """ test id is correct """
        ok = Review()
        var = Review(ok)
        self.assertEqual(type(ok), Review)
        self.assertEqual(str, type(ok.id))
        self.assertEqual(type(var), Review)

    def test_attri(self):
        """Do all required functions exist"""
        self.assertTrue(hasattr(self.Joe, "__str__"))
        self.assertTrue(hasattr(self.Joe, "to_dict"))
        self.assertTrue(hasattr(self.Joe, "save"))
        self.assertTrue(hasattr(self.Joe, "place_id"))
        self.assertTrue(hasattr(self.Joe, "user_id"))
        self.assertTrue(hasattr(self.Joe, "text"))
        self.assertTrue(hasattr(self.Joe, "__class__"))

    def test_type_atttr(self):
        """Testign type of attributes of an insance
        """
        self.assertTrue(type(self.Joe.place_id), str)
        self.assertTrue(type(self.Joe.user_id), str)
        self.assertTrue(type(self.Joe.text), str)

    def test_string(self):
        """testing that it's a string"""
        ok = Review()
        self.assertEqual(issubclass(type(ok), BaseModel), True)
        self.assertEqual(type(ok.place_id), str)
        self.assertEqual(type(ok.user_id), str)
        self.assertEqual(type(ok.text), str)

    def test_creat_update(self):
        """ test updated_at and updated_at """
        ok = Review()
        self.assertEqual(datetime, type(ok.created_at))
        self.assertEqual(datetime, type(ok.updated_at))

    @classmethod
    def tearDownClass(self):
        """deletes self.Joe"""
        del self.Joe

if __name__ == "__main__":
    unittest.main()
