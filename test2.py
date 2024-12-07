from funciones import sumar
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = sumar(2, 4, 5 , 1)
        self.assertEqual(12, resultado)

if __name__ == '__main__':
    unittest.main()