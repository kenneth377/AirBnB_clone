import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_inheritance(self):
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'save'))
        self.assertTrue(hasattr(city, 'to_dict'))

    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
