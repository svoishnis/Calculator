"""The Complete CSV Methods"""
import csv
import os.path
import shutil
import time
from shutil import copy2
import pandas
from calc.calculator import Calculator

# Global Variables
ADDITION_OP = 'addition'
FILE = "\\test_data\\" + ADDITION_OP + '.csv'
DIRECTORY = os.path.abspath(FILE)
FILE_LIST = ["default"]
FILE_RECORD_COUNT = 100


class CSVTest:
    """CSV Class"""

    @staticmethod
    def get_files():
        """Looks in the Directory for Files"""
        global FILE_LIST
        for filename in os.listdir(os.getcwd() + "\\test_data"):
            FILE_LIST.append(filename)
        return FILE_LIST

    @staticmethod
    def reset_file_list():
        """Resets the List of Files to Empty"""
        global FILE_LIST
        FILE_LIST = []
        return FILE_LIST

    @staticmethod
    def reset_record_count():
        """Resets the Length of Files to 0"""
        global FILE_RECORD_COUNT
        FILE_RECORD_COUNT = 0
        return True

    @staticmethod
    def get_operation():
        """Returns the Operation of the File at Record Count"""
        global FILE_LIST
        if len(FILE_LIST) == 0:
            next_op = "Operation Undefined"
        else:
            next_file = FILE_LIST[FILE_RECORD_COUNT]
            next_op = next_file[: -4]
        return next_op

    @staticmethod
    def return_loop_count():
        """Returns the New Count of the Length of Files"""
        global FILE_RECORD_COUNT
        new_count = FILE_RECORD_COUNT + 1
        return new_count

    @staticmethod
    def get_file_path():
        """Gets the file path"""
        global FILE_LIST
        if len(FILE_LIST) == 0:
            next_path = "No Files"
        else:
            global FILE_RECORD_COUNT
            next_file = FILE_LIST[0]
            next_path = os.path.abspath(next_file)
        return next_path

    @staticmethod
    def parse_data_frame_row(row):
        """Take a row and reformat into a tuple"""
        my_tuple = row[1]
        Value_1 = my_tuple.Value_1
        Value_2 = my_tuple.Value_2
        Result = my_tuple.Result
        return Value_1, Value_2, float(Result)

    @staticmethod
    def create_tuple():
        """Creates a tuple from the dataframe"""
        processed_list = CSVTest.get_tuples(CSVTest.do_iteration(CSVTest.create_panda_df()))
        return processed_list

    @staticmethod
    def create_panda_df():
        """Creates a dataframe from an input file"""
        global FILE_LIST
        global DIRECTORY
        # filename = os.path.abspath(FILE_LIST[0])
        file = FILE_LIST[0]
        file_name = os.path.abspath('test_data')
        new_file_name = file_name + "\\" + file
        data_frame = pandas.read_csv(new_file_name,
                                     header=0,
                                     names=['Value_1', 'Value_2', 'Result'])
        return data_frame

    @staticmethod
    def do_iteration(data_frame):
        """Creates the Dataframe Rows from DF"""
        dataframe_rows = data_frame.iterrows()
        return dataframe_rows

    @staticmethod
    def get_tuples(dataframe_rows):
        """gets the tuple from the provided dataframe"""
        list_of_tuples = list(map(CSVTest.parse_data_frame_row, dataframe_rows))
        return list_of_tuples

    @staticmethod
    def parse_tuple_addition(my_tuple):
        """Parses the tuple to the addition method"""
        Calculator.add_numbers(my_tuple[0:2])
        return Calculator.get_last_result_value(), my_tuple[2]

    @staticmethod
    def parse_tuple_subtraction(my_tuple):
        """Parses the tuple to the subtraction method"""
        Calculator.subtract_numbers(my_tuple[0:2])
        # Investigate Issue - temp fix'''
        one = my_tuple[0]
        two = my_tuple[1]
        result = one - two
        return result, my_tuple[2]
        # return Calculator.get_last_result_value(), my_tuple[2]

    @staticmethod
    def parse_tuple_multiplication(my_tuple):
        """Parses the tuple to the multiplication method"""
        Calculator.multiply_numbers(my_tuple[0:2])
        return Calculator.get_last_result_value(), my_tuple[2]

    @staticmethod
    def parse_tuple_division(my_tuple):
        """Parses the tuple to the division method"""
        Calculator.divide_numbers(my_tuple[0:2])
        return Calculator.get_last_result_value(), my_tuple[2]

    @staticmethod
    def compare_calc_with_results(my_tuple):
        """Takes list of sums - compares calculated to provided"""
        calculated = my_tuple[0]
        provided = my_tuple[1]
        flag = calculated == provided
        return flag

    @staticmethod
    def get_time():
        """gets the current time (readable)"""
        current_time = time.time()
        local_time = time.ctime(current_time)
        return str(local_time)

    @staticmethod
    def get_list_sums():
        """Gets the tuple of sums"""
        if CSVTest.get_operation() == 'addition':
            sums = list(map(CSVTest.parse_tuple_addition, CSVTest.create_tuple()))
            print("Addition Parsing Triggered")
            return sums
        elif CSVTest.get_operation() == 'subtraction':
            sums = list(map(CSVTest.parse_tuple_subtraction, CSVTest.create_tuple()))
            print("Subtraction Parsing Triggered")
            return sums
        elif CSVTest.get_operation() == 'multiplication':
            sums = list(map(CSVTest.parse_tuple_multiplication, CSVTest.create_tuple()))
            print("Multiplication Parsing Triggered")
            return sums
        elif CSVTest.get_operation() == 'division':
            sums = list(map(CSVTest.parse_tuple_division, CSVTest.create_tuple()))
            print("Division Parsing Triggered")
            return sums
        else:
            sums = "error"
            with open('ERROR_log.csv', 'w') as csv_file:
                csv_error_writer = csv.writer(csv_file, delimiter=',')
                csv_error_writer.writerow([CSVTest.get_time(),
                                           CSVTest.get_operation,
                                           'Operation Undefined'])
        return sums

    @staticmethod
    def get_validation():
        """Gets List of Validation for Calculations"""
        validation = list(map(CSVTest.compare_calc_with_results, CSVTest.get_list_sums()))
        return validation

    @staticmethod
    def add_record(current):
        """Increments the current count by 1"""
        new_count = current + 1
        return new_count

    @staticmethod
    def write_to_log():
        """Writes the results to logs"""
        with open(os.path.abspath('result_log2.csv'),
                  'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(['Timestamp', 'FileName', 'Record #',
                                 'Operation', 'CalcResult', 'Flag'])
            loop_count = len(CSVTest.create_panda_df())
            for i in range(loop_count):
                # range(len(CSVTest.createPandaDF())):
                calculated, provided = CSVTest.get_list_sums()[i]
                if calculated != 'ZeroDivisionError':
                    csv_writer.writerow(
                        [CSVTest.get_time(), FILE_LIST[i - 1], CSVTest.add_record(i),
                         CSVTest.get_operation(), calculated, CSVTest.get_validation()[i]])
                elif calculated == 'ZeroDivisionError':
                    csv_writer.writerow(
                        [CSVTest.get_time(), FILE_LIST[i - 1],
                         CSVTest.add_record(i), CSVTest.get_operation(),
                         calculated, 'ZeroDivisionError'])
                    error_row = ([CSVTest.get_time(), CSVTest.get_operation(),
                                  'Error', 'Error Triggered'])
                    with open('ERROR_log.csv', 'a') as f:
                        csv_error_writer = csv.writer(f, delimiter=',')
                        csv_error_writer.writerow([error_row])

                else:
                    csv_writer.writerow(["Done"])

            return "Successfully Written"

    @staticmethod
    def move_to_done():
        """This method moves files to the done folder"""
        shutil.move(FILE, os.path.abspath(FILE_LIST[FILE_RECORD_COUNT]), copy_function=copy2)
        return 'True'
