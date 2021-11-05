from src.Stats.Mean import mean
from src.calculator.Addition import addition
from src.calculator.Division import division
from src.calculator.Square import square
from src.calculator.Subtraction import subtraction

def variance(data):
    try:
        length = len(data)
        mean_v = mean(data)
        total = 0
        for x in data:
            x = square(subtraction(mean_v, x))
            total = addition(x, total)
        return division(length-1, total)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Incorrect values were provided")