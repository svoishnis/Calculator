from src.Calculator.Addition import addition
from src.Calculator.Division import division
from src.Calculator.Subtraction import subtraction

def median(data):
    try:
        lst = sorted(data)
        length = len(data)
        if length % 2 == 0: #check for an dataset with an even number of entries
            median1 = lst[int(length // 2)] # First Element of the second half
            median2 = lst[int(subtraction((length //2), 1))] # Last Element of the first half
            actual_median = division(2, addition(median1,median2))
        else:
            actual_median = lst[length // 2] #Entity that is in the middle of a dataset with an off number of entities
            return actual_median
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Incorrect data provided")