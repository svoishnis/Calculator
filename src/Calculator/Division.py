"""This is the function for Division"""
def division(a,b):
    try:
        b = float(b)
        a = float(a)
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            c = float(b) / float(a)
            return c
        #except ZeroDivsionError
        #   print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Incorrect Values were provided")