import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_inheritance(self):
        amenity = Amenity()

        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'save'))
        self.assertTrue(hasattr(amenity, 'to_dict'))

    def test_attributes(self):
        amenity = Amenity()

        self.assertTrue(hasattr(amenity, 'name'))

        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
