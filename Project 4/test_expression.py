import unittest

# Import all classes from the expression.py module:
from expression import *

class Test_Expressions(unittest.TestCase):
    def test_intvalue_init(self):
        obj = IntValue(3)

    def test_binop_init(self):
        obj = BinOp(3, 2)

    def test_add_init(self):
        obj = Add(4, 6)

    def test_add_str(self):
        obj = Add(4, 5)
        self.assertEqual(obj.__str__(), '(4 + 5)')

    def test_add_evaluate(self):
        obj = Add(3, 6)
        self.assertEqual(obj.evaluate(), 9)
        
    def test_sub_init(self):
        obj = Sub(5, 3)

    def test_sub_str(self):
        obj = Sub(10, 5)
        self.assertEqual(obj.__str__(), '(10 - 5)')

    def test_sub_evaluate(self):
        obj = Sub(3, 6)
        self.assertEqual(obj.evaluate(), -3)

    def test_mul_init(self):
        obj = Mul(4, 2)

    def test_mul_str(self):
        obj = Mul(2, 5)
        self.assertEqual(obj.__str__(), '(2 * 5)')

    def test_mul_evaluate(self):
        obj = Mul(3, 6)
        self.assertEqual(obj.evaluate(), 18)

    def test_div_init(self):
        obj = Div(2, 4)

    def test_div_str(self):
        obj = Div(12, 3)
        self.assertEqual(obj.__str__(), '(12 / 3)')

    def test_div_evaluate(self):
        obj = Div(21, 7)
        self.assertEqual(obj.evaluate(), 3)


   


if __name__ == "__main__":
    unittest.main(verbosity=2)