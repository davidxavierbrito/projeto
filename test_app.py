# test_app.py
import unittest
from app import app  # Importa a aplicação Flask

class TestApp(unittest.TestCase):
    
    def setUp(self):
        # Configura a aplicação para testes
        self.app = app.test_client()
        self.app.testing = True

    def test_soma(self):
        # Testando a rota de soma com os parâmetros 'a' e 'b'
        response = self.app.get('/soma?a=2&b=3')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['resultado'], 5)

    def test_subtrai(self):
        # Testando a rota de subtração
        response = self.app.get('/subtrai?a=10&b=4')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['resultado'], 6)

    def test_multiplica(self):
        # Testando a rota de multiplicação
        response = self.app.get('/multiplica?a=5&b=6')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['resultado'], 30)

    def test_divide(self):
        # Testando a rota de divisão
        response = self.app.get('/divide?a=8&b=2')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['resultado'], 4.0)

    def test_divide_por_zero(self):
        # Testando a divisão por zero
        response = self.app.get('/divide?a=5&b=0')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['resultado'], "Erro: Divisão por zero não permitida")

if __name__ == "__main__":
    unittest.main()
