from funciones import dividir
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def setUp(self):
        print("--- setUp")

    def tearDown(self):
        print("--- tearDown")

    def test_1(self):
        print("--- Test: 1")

    def test_2(self):
        print("--- Test: 2")

if __name__ == '__main__':
    unittest.main()