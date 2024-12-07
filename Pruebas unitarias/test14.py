from funciones import dividir, convertir_numero
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
    	with self.assertRaises(ZeroDivisionError):
    		resultado = dividir(0, 0)

    def test_2(self):
    	try:
    		result = convertir_numero("10")
    		self.assertIsInstance(result, int)
    	except ValueError:
    		self.fail()

    def test_3(self):
    	self.assertRaises(ValueError, convertir_numero, "b")

if __name__ == '__main__':
    unittest.main()