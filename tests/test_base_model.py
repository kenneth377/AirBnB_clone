import unittest
from models.base_model import BaseModel
from models.__init__ import storage

class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_str_representation(self):
        obj = BaseModel()
        expected_output = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_output)

    def test_save_method(self):
        obj = BaseModel()
        obj.save()

        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)

        self.assertTrue(isinstance(obj_dict['created_at'], str))
        self.assertTrue(isinstance(obj_dict['updated_at'], str))

if __name__ == '__main__':
    unittest.main()
