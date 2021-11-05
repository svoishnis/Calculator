from src.calculator.Addition import addition
from src.calculator.Subtraction import subtraction
from src.calculator.Multiplication import multiplication
from src.calculator.Division import division
from src.calculator.Square import square
from src.calculator.Squareroot import sqrt

class Calculator: #defines the object
    result = 0    #set value for result

    def __init__(self): #Object Oriented Programming
        pass
    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a, b):
        self.result = square(a, b)
        return self.result

    def sqrt(self, a, b):
        self.result = sqrt(a, b)
        return self.result