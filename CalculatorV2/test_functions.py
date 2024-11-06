import unittest
from functions import *

class TestOperators(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 12), 22)
        self.assertEqual(add(100, 200), 300)
        self.assertEqual(add(32, 35), 67)


    def test_subtract(self):
        self.assertEqual(subtract(50, 25), 25)
        self.assertEqual(subtract(13, 7), 6)
        self.assertEqual(subtract(90, 40), 50)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(2, 10), 20)
        self.assertEqual(multiply(10, 10), 100) 

    def test_divide(self):
        self.assertEqual(divide(15, 5), 3)      
        self.assertEqual(divide(15, 5), 3)


    def divide_by_zero(self):        
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()