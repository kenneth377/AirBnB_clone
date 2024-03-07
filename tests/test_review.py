import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_inheritance(self):
        review = Review()
        
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'save'))
        self.assertTrue(hasattr(review, 'to_dict'))

    def test_attributes(self):
        review = Review()

        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()
