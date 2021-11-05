from src.calculator.Addition import addition
from src.calculator.Division import division

def mean(data):
    try:
        total = 0
        length = len(data)
        for num in data:
            total = addition(total, num)
            return division(length, total)
    except  ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Incorrect data given")