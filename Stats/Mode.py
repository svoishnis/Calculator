from collections import Counter

def mode(data):
    try:
        length = len(data) # Calculates the length of the dataset
        count = Counter(data) #Counts keys and values
        get_mode = dict(count) #Splits count into dictonary
        mode_lst = [k for k, v in get_mode.items() if v == max(list(count.values()))] # Iterates through the mode_dict
        print(type(mode_lst))
        if len(mode_lst) == length:
            get_mode = "No mode was found"
        else:
            get_mode = mode_lst[0]
            return get_mode
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Incorrect values were provided ")