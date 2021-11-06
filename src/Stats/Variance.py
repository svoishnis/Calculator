from src.Stats.Mean import mean
from src.Calculator.Addition import addition
from src.Calculator.Division import division
from src.Calculator.Square import square
from src.Calculator.Subtraction import subtraction


def variance(data):
    try:
        length = len(data)
        mean_v = mean(data)
        total = 0
        for x in data:
            x = square(subtraction(mean_v, x))
            total = addition(x, total)
        return division(length - 1, total)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Incorrect values were provided")
