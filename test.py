import unittest
from main import add, subtract, multiply, divide, remainder

class TestMath(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 5),7)
       self.assertNotEqual(add(3, 7), 9)

   def test_subtract(self):
       self.assertEqual(subtract(7, 4), 3)
       self.assertNotEqual(subtract(4, 2), 1)

   def test_multiply(self):
       self.assertNotEqual(multiply(2, 5), 12)
       self.assertEqual(multiply(3, 6), 18)

   def test_divide(self):
       self.assertNotEqual(divide(4, 2), 3)
       self.assertEqual(divide(20, 5), 4)

   def test_positive_numbers(self):
       self.assertEqual(remainder(10, 3), 1)
       self.assertEqual(remainder(15, 4), 3)

   def test_negative_numbers(self):
       self.assertEqual(remainder(-10, 3), 2)
       self.assertEqual(remainder(10, -3), -2)

   def test_zero_dividend(self):
       self.assertEqual(remainder(0, 5), 0)  

   def test_division_by_zero(self):
       with self.assertRaises(ZeroDivisionError):
           remainder(10, 0)
       with self.assertRaises(ZeroDivisionError):
           remainder(0, 0)


if __name__ == '__main__':
   unittest.main()

