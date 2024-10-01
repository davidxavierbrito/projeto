# test_app.py
import unittest
from app import soma

class TestApp(unittest.TestCase):
    def test_soma(self):
        """Testa se a função soma funciona corretamente."""
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
