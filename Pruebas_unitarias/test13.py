import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        empleado = "aaa"
        self.assertNotIsInstance(empleado, int) #or (str, int, float)

if __name__ == '__main__':
    unittest.main()