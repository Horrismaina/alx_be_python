# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a fresh calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=1)

    def test_subtraction(self):
        """Test the subtract method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(3.5, 2.5), 1.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=1)

    def test_multiplication(self):
        """Test the multiply method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertEqual(self.calc.multiply(1, 0), 0)

    def test_division(self):
        """Test the divide method with various scenarios."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(6, -2), -3)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.divide(5.0, 2.0), 2.5)
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))

    def test_floating_point_precision(self):
        """Test handling of floating point precision."""
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333333, places=5)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.1), 0.01, places=2)

if __name__ == '__main__':
    unittest.main()