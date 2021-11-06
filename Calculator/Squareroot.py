"""This function takes the square root of the input value"""


def sqrt(a):
    a = float(a)
    if a >= 0:
        return round(float(a) ** .5, 10)
    else:
        raise ValueError("Input needs to be a non-negative integer")
