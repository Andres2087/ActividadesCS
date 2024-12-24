from funciones import devolver_variable
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        var = [3, 4]
        resultado = devolver_variable(var)
        self.assertIs(var, resultado)

if __name__ == '__main__':
    unittest.main()