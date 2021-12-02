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
            nextOp = "Operation Undefined"
        else:
            nextfile = FILE_LIST[FILE_RECORD_COUNT]
            nextOp = nextfile[: -4]
        return nextOp

    @staticmethod
    def return_loop_count():
        """Returns the New Count of the Length of Files"""
        global FILE_RECORD_COUNT
        newCount = FILE_RECORD_COUNT + 1
        return newCount

    @staticmethod
    def get_file_path():
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
        processed_list = CSVTest.get_tuples(CSVTest.do_iteration(CSVTest.create_panda_df()))
        return processed_list

    @staticmethod
    def create_panda_df():
        global FILE_LIST
        global DIRECTORY
        # filename = os.path.abspath(FILE_LIST[0])
        file = FILE_LIST[0]
        filename = os.path.abspath('test_data')
        newfilename = filename + "\\" + file
        data_frame = pandas.read_csv(newfilename,
                                     header=0,
                                     names=['Value_1', 'Value_2', 'Result'])
        return data_frame

    @staticmethod
    def do_iteration(df):
        """Creates the Dataframe Rows from DF"""
        dataframe_rows = df.iterrows()
        return dataframe_rows

    @staticmethod
    def get_tuples(dataframe_rows):
        list_of_tuples = list(map(CSVTest.parse_data_frame_row, dataframe_rows))
        return list_of_tuples

    @staticmethod
    def parse_tuple_addition(mTuple):
        Calculator.add_numbers(mTuple[0:2])
        return Calculator.get_last_result_value(), mTuple[2]

    @staticmethod
    def parse_tuple_subtraction(mTuple):
        Calculator.subtract_numbers(mTuple[0:2])
        # Investigate Issue - temp fix'''
        one = mTuple[0]
        two = mTuple[1]
        result = one - two
        return result, mTuple[2]
        # return Calculator.get_last_result_value(), mTuple[2]

    @staticmethod
    def parse_tuple_multiplication(mTuple):
        Calculator.multiply_numbers(mTuple[0:2])
        return Calculator.get_last_result_value(), mTuple[2]

    @staticmethod
    def parse_tuple_division(mTuple):
        Calculator.divide_numbers(mTuple[0:2])
        return Calculator.get_last_result_value(), mTuple[2]

    @staticmethod
    def compare_calc_with_results(mTuple):
        calculated = mTuple[0]
        provided = mTuple[1]
        flag = calculated == provided
        return flag

    @staticmethod
    def get_time():
        current_time = time.time()
        local_time = time.ctime(current_time)
        return str(local_time)

    @staticmethod
    def get_list_sums():
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
            with open('ERROR_log.csv', 'w') as csvfile:
                csverrorwriter = csv.writer(csvfile, delimiter=',')
                csverrorwriter.writerow([CSVTest.get_time(), CSVTest.get_operation, 'Operation Undefined'])
        return sums

    @staticmethod
    def get_validation():
        """Gets List of Validation for Calculations"""
        validation = list(map(CSVTest.compare_calc_with_results, CSVTest.get_list_sums()))
        return validation

    @staticmethod
    def add_record(current):
        new_count = current + 1
        return new_count

    @staticmethod
    def write_to_log():
        with open(os.path.abspath('result_log2.csv'), 'w') as csvfile:
            global FILE_LIST
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(['Timestamp', 'FileName', 'Record #', 'Operation', 'CalcResult', 'Flag'])
            loop_count = len(CSVTest.create_panda_df())
            for i in range(loop_count):
                # range(len(CSVTest.createPandaDF())):
                a, b = CSVTest.get_list_sums()[i]
                if a != 'ZeroDivisionError':
                    csvwriter.writerow(
                        [CSVTest.get_time(), FILE_LIST[i - 1], CSVTest.add_record(i),
                         CSVTest.get_operation(), a, CSVTest.get_validation()[i]])
                elif a == 'ZeroDivisionError':
                    csvwriter.writerow(
                        [CSVTest.get_time(), FILE_LIST[i - 1], CSVTest.add_record(i), CSVTest.get_operation(), a,
                         'ZeroDivisionError'])
                    error_row = ([CSVTest.get_time(), CSVTest.get_operation(), 'Error', 'Error Triggered'])
                    with open('ERROR_log.csv', 'a') as f:
                        csverrorwriter = csv.writer(f, delimiter=',')
                        csverrorwriter.writerow([error_row])

                else:
                    csvwriter.writerow(["Done"])

            return "Successfully Written"

    @staticmethod
    def move_to_done():
        """This method moves files to the done folder"""
        shutil.move(FILE, os.path.abspath(FILE_LIST[FILE_RECORD_COUNT]), copy_function=copy2)
        return 'True'
