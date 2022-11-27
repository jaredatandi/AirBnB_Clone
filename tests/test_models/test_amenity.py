#!/usr/bin/python3
"""Unittest for Amenity
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test for Amenity"""

    @classmethod
    def setUpClass(self):
        """Instances for testing on"""
        self.amen1 = Amenity()
        self.amen1.name = "Free Wi-Fi"
        self.amen2 = Amenity()
        self.amen2.name = "Parking"

    def test_type_instance(self):
        """Test for type of instance
        """
        self.assertTrue(type(self.amen1), Amenity)

    def test_type(self):
        """Do all required functions exist"""
        self.assertTrue(hasattr(self.amen1, "__str__"))
        self.assertTrue(hasattr(self.amen1, "to_dict"))
        self.assertTrue(hasattr(self.amen1, "name"))
        self.assertTrue(hasattr(self.amen1, "save"))
        self.assertTrue(hasattr(self.amen1, "__class__"))
        self.assertEqual(type(self.amen1.name), str)

    def test_is_subclass(self):
        """Tests to see if Amenity is a subclass of BaseModel"""
        ok = Amenity()
        self.assertEqual(issubclass(type(ok), BaseModel), True)

    def test_instance(self):
        """Test if instance of class works as intented"""
        self.assertIsInstance(self.amen1, Amenity)
        self.assertIsInstance(self.amen1.name, str)
        self.assertIsInstance(self.amen2, Amenity)
        self.assertIsInstance(self.amen2.name, str)

    def test_id(self):
        """ test id is correct """
        ok = Amenity()
        self.assertEqual(str, type(ok.id))
        self.assertEqual(type(ok), Amenity)
        self.assertEqual(type(ok.id), str)

    def test_to_dict(self):
        """Test to_dict method"""
        ok = Amenity()
        self.assertEqual(ok.__class__.__name__, "Amenity")
        self.assertTrue(ok.to_dict()["created_at"], str)
        self.assertTrue(ok.to_dict()["updated_at"], str)

    def test_created_at(self):
        """ test created_at and update_at as well """
        ok = Amenity()
        self.assertEqual(datetime, type(ok.created_at))
        self.assertEqual(datetime, type(ok.updated_at))

    def test_dict_to(self):
        """ test if dictionary"""
        ok = Amenity()
        var = ok.to_dict()
        foo = Amenity(var)
        self.assertEqual(type(var), dict)
        self.assertTrue(hasattr(foo, "__class__"))
        self.assertTrue(hasattr(foo, "__str__"))
        self.assertTrue(hasattr(foo, "to_dict"))
        self.assertTrue(hasattr(foo, "name"))
        self.assertTrue(hasattr(foo, "save"))
        self.assertTrue(hasattr(foo, "__class__"))

    @classmethod
    def tearDownClass(self):
        """Tears it all down by deleting instances"""
        del self.amen1
        del self.amen2

if __name__ == "__main__":
    unittest.main()
