from funciones import devolver_none
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = devolver_none("Prueba")
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()