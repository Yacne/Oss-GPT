import unittest
from utils import normalize_text

class TestUtils(unittest.TestCase):
    def test_normalize_text(self):
        self.assertEqual(normalize_text("أهلاً! كيف حالك؟"), "أهلاً كيف حالك")
        self.assertEqual(normalize_text("مساء الخير..."), "مساء الخير")