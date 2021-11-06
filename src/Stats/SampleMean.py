import random
from src.Calculator.Addition import addition
from src.Calculator.Division import division


def sample_mean(data, sample_size):
    try:
        total = 0
        random_values = random.choices(data, sample_size)
        length = len(random_values)
        for num in random_values:
            total = addition(total, num)
            return division(total, length)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Incorrect values were provided")
