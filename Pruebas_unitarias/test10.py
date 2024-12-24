from funciones import devolver_variable
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = devolver_variable([1, 5, 6, 3, 9])
        self.assertIn(9, resultado)

if __name__ == '__main__':
    unittest.main()