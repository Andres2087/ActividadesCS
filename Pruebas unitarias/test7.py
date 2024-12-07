from funciones import devolver_variable
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        var = [3, 4]
        resultado = devolver_variable(var)
        self.assertIsNot(var[0], resultado)

if __name__ == '__main__':
    unittest.main()