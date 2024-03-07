import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_inheritance(self):
        state = State()

        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'save'))
        self.assertTrue(hasattr(state, 'to_dict'))

    def test_attributes(self):
        state = State()

        self.assertTrue(hasattr(state, 'name'))

        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
