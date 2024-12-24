from funciones import devolver_none
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = devolver_none("Pru")
        self.assertIsNotNone(resultado)

if __name__ == '__main__':
    unittest.main()