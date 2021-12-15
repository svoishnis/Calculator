import csv
import time
from calc.calculator import Calculator

OPERATION_CSV = "test"
DATA = []


class CsvPostLogic:

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

    @staticmethod
    def read_file(f):
        with open(f.filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            data = [tuple(line) for line in reader]
        return data

    @staticmethod
    def store_output_data(output, *args):
        global DATA
        DATA = output
        return True

    @staticmethod
    def get_output_data():
        global DATA
        return DATA

    @staticmethod
    def write_to_file():
        global DATA
        with open('result.csv', mode='w', newline='') as result_file:
            result_writer = csv.writer(result_file, delimiter=',',
                                       escapechar='"', quoting=csv.QUOTE_NONE)
            header = ["Value 1", "Value 2", "Operation", "Result Provided", "Calculated Result", "Validation"]
            result_writer.writerow(header)
            for row in CsvPostLogic.get_output_data():
                result_writer.writerow(row)
            result_writer.writerow(['Timestamp: ' + CsvPostLogic.get_time()])
            result_writer.writerow(['Operation: ' + CsvPostLogic.get_operation()])
            # CsvPostLogic.store_output_data(my_tuple2)
            result_file.close()
        return True
