# test_app.py
import unittest
from app import soma, subtrai, multiplica, divide

class TestApp(unittest.TestCase):
    def test_soma(self):
        """Testa se a função soma funciona corretamente."""
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)
    
    def test_subtrai(self):
        """Testa se a função subtrai funciona corretamente."""
        self.assertEqual(subtrai(10, 4), 6)
        self.assertEqual(subtrai(0, 0), 0)
        self.assertEqual(subtrai(5, 10), -5)
    
    def test_multiplica(self):
        """Testa se a função multiplica funciona corretamente."""
        self.assertEqual(multiplica(2, 3), 6)
        self.assertEqual(multiplica(0, 10), 0)
        self.assertEqual(multiplica(-1, 5), -5)
    
    def test_divide(self):
        """Testa se a função divide funciona corretamente."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(3, 1), 3)
        self.assertEqual(divide(5, 0), "Erro: e Divisão por zero não permitida")
        self.assertEqual(divide(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
