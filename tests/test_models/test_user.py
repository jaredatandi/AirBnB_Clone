#!/usr/bin/python3
"""Unitest user"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class test_user(unittest.TestCase):
    """Unitest user"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.foo = User()

    def test_inst(self):
        """some tests for instance"""
        self.assertTrue(type(self.foo), User)
        self.assertTrue(type(self.foo.email), str)
        self.assertTrue(type(self.foo.password), str)
        self.assertTrue(type(self.foo.first_name), str)
        self.assertTrue(type(self.foo.last_name), str)

    def test_to_dict(self):
        """testing to_dict method"""
        self.assertEqual('to_dict' in dir(self.foo), True)

    def test_subclass(self):
        """testing if subclass"""
        self.assertTrue(issubclass(self.foo.__class__, BaseModel), True)

    def test_is_subclass(self):
        """Tests to see if User is a subclass of BaseModel"""
        ok = User()
        self.assertEqual(issubclass(type(ok), BaseModel), True)

    def test_save(self):
        """Test if is properly saved or not"""
        ok = User()
        ok.save()
        self.assertNotEqual(ok.created_at, ok.updated_at)

    def test_id(self):
        """ test for valid id"""
        ok = User()
        self.assertEqual(str, type(ok.id))
        self.assertEqual(type(ok), User)

    def test_created_at(self):
        """ test created_at and update_at as well"""
        ok = User()
        self.assertEqual(datetime, type(ok.created_at))
        self.assertEqual(datetime, type(ok.updated_at))

    def test_existance(self):
        """Do all required functions exist"""
        ok = User()
        self.assertTrue(hasattr(ok, "__str__"))
        self.assertTrue(hasattr(ok, "to_dict"))
        self.assertTrue(hasattr(ok, "save"))
        self.assertTrue(hasattr(ok, "email"))
        self.assertTrue(hasattr(ok, "password"))
        self.assertTrue(hasattr(ok, "first_name"))
        self.assertTrue(hasattr(ok, "last_name"))
        self.assertTrue(hasattr(ok, "__class__"))

    @classmethod
    def tearDown(self):
        """tearing it down by deleting self.foo"""
        del self.foo

if __name__ == "__main__":
    unittest.main()
