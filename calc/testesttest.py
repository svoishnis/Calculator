import time
from calc.calculator import Calculator


class CsvPostLogic:
    OPERATION_CSV = "test"

    def convert_input_row_into_output_row(self, csv_row):
        """Methods coverts the input row into output row"""
        Calculator.addition(csv_row)
        my_tuple1 = (csv_row[0], csv_row[1])
        CsvPostLogic.determine_calculation(my_tuple1)
        calc = Calculator.get_last_result_value()
        operation = CsvPostLogic.get_operation()
        if calc == float(csv_row[2]):
            result = "Pass"
        else:
            result = "Fail"
        return csv_row[0], csv_row[1], operation, csv_row[2], calc, result

    @staticmethod
    def set_operation(op):
        global OPERATION_CSV
        OPERATION_CSV = op
        return True

    @staticmethod
    def get_operation():
        global OPERATION_CSV
        return OPERATION_CSV

    @staticmethod
    def determine_calculation(my_tuple1):
        op = CsvPostLogic.get_operation()
        if op == "addition":
            Calculator.addition(my_tuple1)
        elif op == "subtraction":
            Calculator.subtraction(my_tuple1)
        elif op == "multiplication":
            Calculator.multiplication(my_tuple1)
        elif op == "division":
            Calculator.division(my_tuple1)
        else:
            return "Error"
        return "True"

    @staticmethod
    def get_time():
        """gets the current time (readable)"""
        current_time = time.time()
        local_time = time.ctime(current_time)
        return str(local_time)
