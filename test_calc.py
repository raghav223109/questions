import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
    def test_sub(self):
        self.assertEqual(calc.sub(1, 2), -1)
    def test_mul(self):
        self.assertEqual(calc.mul(1, 2), 2)
    def test_div(self):
        self.assertEqual(calc.div(1, 2), 0.5)

if __name__ == '__main__':
    unittest.main()