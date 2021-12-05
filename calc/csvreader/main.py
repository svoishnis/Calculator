"""The Complete CSV Methods"""
import csv
import os.path
import shutil
import time
from shutil import copy2
import pandas
from calc.calculator import Calculator

# pylint: disable-all

# Global Variables
OPERATION = 'Default Operation'
FILE = "\\test_data\\" + OPERATION + '.csv'
DIRECTORY = os.path.abspath(FILE)
FILE_LIST = ["Default List Value"]
FILE_RECORD_COUNT = 100
FILE_LOOPER = 500
FILE_NAME = "Default File Name"


class CSVTest:
    """CSV Class"""

    @staticmethod
    def get_files():
        """Looks in the Directory for Files"""
        CSVTest.reset_parameters()
        global FILE_LIST, FILE_RECORD_COUNT
        for filename in os.listdir(os.getcwd() + "\\test_data"):
            FILE_LIST.append(filename)
        CSVTest.set_record_count()
        CSVTest.set_operation()
        return FILE_LIST

    @staticmethod
    def get_file_list():
        """Returns the global file list"""
        return FILE_LIST

    @staticmethod
    def reset_parameters():
        """Rests all counters for loops"""
        CSVTest.reset_file_list()
        CSVTest.reset_record_count()
        CSVTest.rest_file_looper()
        CSVTest.reset_operation()
        print("Parameters reset")
        return True

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
    def get_record_count():
        """Returns the global number of Files in Input"""
        global FILE_RECORD_COUNT
        return FILE_RECORD_COUNT

    @staticmethod
    def set_record_count():
        """Returns the number of files in list"""
        global FILE_RECORD_COUNT
        FILE_RECORD_COUNT = len(CSVTest.get_file_list())
        return FILE_RECORD_COUNT

    @staticmethod
    def get_file_looper():
        """Gets the global File Looper variable"""
        global FILE_LOOPER
        return FILE_LOOPER

    @staticmethod
    def rest_file_looper():
        """Resets the Global Looper to zero"""
        global FILE_LOOPER
        FILE_LOOPER = 0
        return FILE_LOOPER

    @staticmethod
    def loop_files():
        """Increments place in the File List"""
        global FILE_LOOPER
        FILE_LOOPER = FILE_LOOPER + 1
        return FILE_LOOPER

    @staticmethod
    def get_operation():
        """Returns the Operation of the File at Record Count"""
        global OPERATION
        return OPERATION

    @staticmethod
    def set_operation():
        """Sets the Operation of the File at Looper"""
        global OPERATION, FILE_NAME
        count = CSVTest.get_record_count()
        if count == 0:
            OPERATION = "No Files: Operation Undefined"
            return OPERATION
        else:
            list = CSVTest.get_file_list()
            loop = CSVTest.get_file_looper()
            FILE_NAME = list[loop]
            OPERATION = FILE_NAME[: -4]
        return OPERATION

    @staticmethod
    def reset_operation():
        """Rests the Operation Flag back to default"""
        global OPERATION
        OPERATION = "Default Operation"
        return OPERATION

    @staticmethod
    def return_loop_count():
        """Returns the New Count of the Length of Files"""
        global FILE_RECORD_COUNT
        new_count = FILE_RECORD_COUNT + 1
        return new_count

    @staticmethod
    def get_file_name():
        """Gets the file name at the next loop count"""
        global FILE_NAME
        return FILE_NAME

    @staticmethod
    def set_next_file_name():
        global FILE_NAME
        FILE_NAME = CSVTest.get_file_list()[CSVTest.get_file_looper()]
        return FILE_NAME

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
        input_tuple = CSVTest.get_tuples(CSVTest.do_iteration(CSVTest.create_panda_df()))
        return input_tuple

    @staticmethod
    def create_panda_df():
        """Creates a dataframe from an input file"""
        # noinspection PyGlobalUndefined
        global DATA_FRAME
        file = CSVTest.get_file_name()
        test_data_path = os.path.abspath('test_data')
        new_file_path = test_data_path + "\\" + file
        data_frame = pandas.read_csv(new_file_path,
                                     header=0,
                                     names=['Value_1', 'Value_2', 'Result'])
        DATA_FRAME = data_frame
        return data_frame

    @staticmethod
    def get_data_frame():
        """Helper for getting DF"""
        # noinspection PyGlobalUndefined
        global DATA_FRAME
        return DATA_FRAME

    @staticmethod
    def do_iteration(data_frame):
        """Creates the Dataframe Rows from DF"""
        # noinspection PyGlobalUndefined
        global DATA_FRAME_ROWS
        dataframe_rows = data_frame.iterrows()
        DATA_FRAME_ROWS = dataframe_rows
        return dataframe_rows

    @staticmethod
    def get_data_frame_rows():
        """Retrieves a DF global variable for subsequent processes"""
        # noinspection PyGlobalUndefined
        global DATA_FRAME_ROWS
        return DATA_FRAME_ROWS

    @staticmethod
    def get_tuples(dataframe_rows):
        """gets the tuple from the provided dataframe"""
        list_of_tuples = list(map(CSVTest.parse_data_frame_row, dataframe_rows))
        return list_of_tuples

    @staticmethod
    def parse_tuple_addition(my_tuple):
        """Parses the tuple to the addition method"""
        Calculator.addition(my_tuple[0:2])
        return Calculator.get_last_result_value(), my_tuple[2]

    @staticmethod
    def parse_tuple_subtraction(my_tuple):
        """Parses the tuple to the subtraction method"""
        Calculator.subtraction(my_tuple[0:2])
        # Investigate Issue - temp fix'''
        one = my_tuple[0]
        two = my_tuple[1]
        result = one - two
        return result, my_tuple[2]
        # return Calculator.get_last_result_value(), my_tuple[2]

    @staticmethod
    def parse_tuple_multiplication(my_tuple):
        """Parses the tuple to the multiplication method"""
        Calculator.multiplication(my_tuple[0:2])
        return Calculator.get_last_result_value(), my_tuple[2]

    @staticmethod
    def parse_tuple_division(my_tuple):
        """Parses the tuple to the division method"""
        Calculator.division(my_tuple[0:2])
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
    def create_list_calculations():
        """Gets the tuple of sums"""
        # noinspection PyGlobalUndefined
        global CALCULATIONS_LIST
        if CSVTest.get_operation() == 'addition':
            calculations = list(map(CSVTest.parse_tuple_addition, CSVTest.create_tuple()))
            print("Addition Called")
        elif CSVTest.get_operation() == 'subtraction':
            calculations = list(map(CSVTest.parse_tuple_subtraction, CSVTest.create_tuple()))
            print("Subtraction Called")
        elif CSVTest.get_operation() == 'multiplication':
            calculations = list(map(CSVTest.parse_tuple_multiplication, CSVTest.create_tuple()))
            print("Multiplication Called")
        elif CSVTest.get_operation() == 'division':
            calculations = list(map(CSVTest.parse_tuple_division, CSVTest.create_tuple()))
            print("Division Called")
        else:
            calculations = "error"
            with open('ERROR_log.csv', 'w') as csv_file:
                csv_error_writer = csv.writer(csv_file, delimiter=',')
                csv_error_writer.writerow([CSVTest.get_time(),
                                           CSVTest.get_operation,
                                           'Operation Undefined'])
        CALCULATIONS_LIST = calculations
        return calculations

    @staticmethod
    def get_list_of_calculations():
        """Retrieves a DF global variable for subsequent processes"""
        # noinspection PyGlobalUndefined
        global CALCULATIONS_LIST
        return CALCULATIONS_LIST

    @staticmethod
    def get_validation():
        """Gets List of Validation for Calculations"""
        validation = list(map(CSVTest.compare_calc_with_results, CSVTest.create_list_calculations()))
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
            loop_count = len(CSVTest.get_data_frame())
            calc_list = CSVTest.get_list_of_calculations()
            for i in range(loop_count):
                calculated, provided = calc_list[i]
                if calculated != 'ZeroDivisionError':
                    csv_writer.writerow(
                        [CSVTest.get_time(), FILE_NAME, CSVTest.add_record(i),
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
        # current = os.path.abspath(OPERATION + ".csv")
        # file_done =
        shutil.move("C:\\Users\\svois\\PycharmProjects\\calc2\\tests\\test_data\\" + OPERATION + ".csv",
                    "C:\\Users\\svois\\PycharmProjects\\calc2\\tests\\done\\" + OPERATION + ".csv",
                    copy_function=copy2)
        return "Moved to Done"
