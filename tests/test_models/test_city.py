#!/usr/bin/python3
"""tests for city"""
import unittest
from models.base_model import BaseModel
from models.city import City


class test_city(unittest.TestCase):
    """tests for ciy"""

    @classmethod
    def setUp(self):
        """Setting up"""
        self.cityy = City()
        self.cityy.name = "SF"
        self.cityy.state_id = "OR"

    def type_instance(self):
        """Testing type of instance
        """
        self.assertTrue(type(self.city), City)

    def test_city(self):
        """some tests for instance of city"""
        self.assertTrue(type(self.cityy), City)
        self.assertTrue(type(self.cityy.state_id), str)
        self.assertTrue(type(self.cityy.name), str)

    def test_has_attr(self):
        """some tests for instance of city"""
        self.assertTrue('id' in self.cityy.__dict__)
        self.assertTrue('created_at' in self.cityy.__dict__)
        self.assertTrue('updated_at' in self.cityy.__dict__)
        self.assertTrue('state_id' in self.cityy.__dict__)
        self.assertTrue('name' in self.cityy.__dict__)

    def test_save(self):
        """testing save method"""
        self.cityy.save()
        self.assertNotEqual(self.cityy.created_at, not (self.cityy.updated_at))

    def test_is_subclass(self):
        """Tests to see if City is a subclass of BaseModel"""
        ok = City()
        self.assertEqual(issubclass(type(ok), BaseModel), True)

    def test_id(self):
        """ test id is correct """
        ok = City()
        self.assertEqual(str, type(ok.id))
        self.assertEqual(type(ok), City)

    def test_docs(self):
        """test that all is documented"""
        self.assertTrue(City.__doc__)

    def test_to_dict(self):
        """Test to_dict method"""
        ok = City()
        self.assertEqual(ok.__class__.__name__, "City")
        self.assertTrue(ok.to_dict()["created_at"], str)
        self.assertTrue(ok.to_dict()["updated_at"], str)

    def test_existance(self):
        """Do all required functions exist"""
        self.assertTrue(hasattr(self.cityy, "__str__"))
        self.assertTrue(hasattr(self.cityy, "to_dict"))
        self.assertTrue(hasattr(self.cityy, "name"))
        self.assertTrue(hasattr(self.cityy, "save"))
        self.assertTrue(hasattr(self.cityy, "state_id"))
        self.assertTrue(hasattr(self.cityy, "__class__"))
        self.assertTrue(type(self.cityy.name), str)
        self.assertTrue(type(self.cityy.state_id), str)

    @classmethod
    def tearDown(self):
        """deletes self.cityy"""
        del self.cityy

if __name__ == "__main__":
    unittest.main()
