# Run with python test_parser.py or Run->test_parser.py in CR
import unittest

# Import all classes from the parser.py module, you may also 
# wish to import things from expression.py
from parser import *

class Test_Parser(unittest.TestCase):
    
    def test_parser_init(self):
        """Tests the instantiation of Parser class"""
        obj = Parser()

    def test_parser_expression(self):
        obj = Parser()
        self.assertEqual(obj.parse('3 4 -'))
    

if __name__ == "__main__":
    unittest.main(verbosity=2)