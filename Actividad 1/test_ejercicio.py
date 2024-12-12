from ejercicio import total, addit, mult, divide, length, reverse, remove_letter, max, even_numbers, odd_numbers, is_even 
import unittest

class Tests(unittest.TestCase):
    
    def test_total(self):
        lst=[4,1,2,7]
        res = total(lst)
        self.assertEqual(14, res)

    def test_addit(self):
        res = addit(2)
        self.assertEqual(7, res)

    def test_mult(self):
        res = mult(6)
        self.assertEqual(66, res)

    def test_divide(self):
        res = divide(20, 4)
        self.assertEqual(5, res)

    def test_length_less_than_5(self):
        res = length([4, 1, 8, 5])
        self.assertEqual("Less than 5", res)

    def test_length_longer_than_5(self):
        res = length("Cancion")
        self.assertEqual("Longer than 5", res)

    def test_reverse(self):
        res = reverse("azul")
        self.assertEqual("luza", res)

    def test_remove_letter(self):
        res = remove_letter("o", "Cuanto dinero gastaste")
        self.assertEqual("Cuant diner gastaste", res)

    def test_max(self):
        res = max([8, 2, 15, 9, 12])
        self.assertEqual(15, res)
    
    def test_even_numbers(self):
        res = even_numbers([3, 12, 5, 2, 26, 11])
        self.assertEqual([12, 2, 26], res)
    
    def test_odd_numbers(self):
        res = odd_numbers([3, 12, 5, 2, 26, 11])
        self.assertEqual([3, 5, 11], res)
    
    def test_is_even_true(self):
        res = is_even(4)
        self.assertTrue(res)
    
    def test_is_even_false(self):
        res = is_even(37)
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()