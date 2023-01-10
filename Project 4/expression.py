"""expression.py
Expression and BinOp abstract classes and their concrete subclasses for 
representing integer expressions containing +, -, *, /
"""

import logging
# To suppress DEBUG messages, level = logging.INFO
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('expression.py')

class Expression:
    """The abstract (base) class for all other expression node classes."""
    def __init__(self):
        log.debug(f"{self.__class__.__name__} created")
        pass
    
    def __str__(self) -> str:
        raise NotImplementedError("__str__() is not implemented")
    
    def evaluate(self) -> int:
        raise NotImplementedError("evaluate() is not implemented")

class IntValue(Expression):
    """Class for Integer Values in expression"""

    def __init__(self, val: int):
        """Instantiates an integer for expression"""
        self.val = val
        
    def __str__(self) -> str:
        """String representation of integer in expression"""
        return f'{self.val}'
    
    def evaluate(self) -> int:
        """Returns integer in expression"""
        return self.val

class BinOp(Expression):
    """Class for Binary Operator"""
    def __init__(self, left: Expression, right: Expression):
        """ """
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """Recursively prints each of its children subtrees"""
        result: str = str(self.val)
        if self.left is not None:
            result += str(self.left)
        if self.right is not None:
            result += str(self.right)
        return result

    def evaluate(self) -> int:
        """Not Implemented in this class"""
        raise NotImplementedError

class Add(BinOp):
    """Addition node Class for expression"""

    def __init__(self, left: Expression, right: Expression):
        """Instantiates addition expression"""
        super().__init__(left, right)

    def __str__(self) -> str:
        """String representation of addition expression"""
        return '(' + str(self.left) +' '+ '+' + ' ' + str(self.right) + ')'

    def evaluate(self) -> int:
        """ """
        return int(self.left) + int(self.right)

class Sub(BinOp):
    """Subtraction node Class for expression"""

    def __init__(self, left: Expression, right: Expression):
        """Instantiates subtraction expression"""
        super().__init__(left, right)
    
    def __str__(self) -> str:
        """String representation of subtraction expression"""
        return '(' + str(self.left) +' '+ '-' + ' ' + str(self.right) + ')'

    def evaluate(self) -> int:
        """ """
        return int(self.left) - int(self.right)

class Mul(BinOp):
    """Multiplication node Class for expression"""

    def __init__(self, left: Expression, right: Expression):
        """Instantiates multiplication expression"""
        super().__init__(left, right)
    
    def __str__(self) -> str:
        """String representation of multiplication expression"""
        return '(' + str(self.left) +' '+ '*' + ' ' + str(self.right) + ')'

    def evaluate(self) -> int:
        """ """
        return int(self.left) * int(self.right)

class Div(BinOp):
    """Division node Class for expression"""

    def __init__(self, left: Expression, right: Expression):
        """Instantiates division expression"""
        super().__init__(left, right)
    
    def __str__(self) -> str:
        """String representation of division expression"""
        return '(' + str(self.left) +' '+ '/' + ' ' + str(self.right) + ')'

    def evaluate(self) -> int:
        """ """
        return int(self.left) / int(self.right)

