from src.Calculator.Squareroot import sqrt
from src.Stats.Variance import variance


def std(variance_num):
    try:
        variance_num = variance(variance_num)
        return sqrt(variance_num)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Incorrect values were provided")
