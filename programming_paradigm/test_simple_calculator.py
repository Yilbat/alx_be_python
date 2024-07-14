import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc =SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
    def test_substraction(self):
        self.assertEqual(self.calc.subtract(2,3),5)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3),5)
    def test_division(self):
        self.assertEqual(self.calc.divide(2,3),5)
        self.assertEqual(self.calc.divide(2,0),ZeroDivisionError)

   