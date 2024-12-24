import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        empleado = "aaa"
        self.assertIsInstance(empleado, str) #or (str, int, float)

if __name__ == '__main__':
    unittest.main()