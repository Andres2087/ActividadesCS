from funciones import mayor_edad
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = mayor_edad(21)
        self.assertTrue(resultado)

if __name__ == '__main__':
    unittest.main()