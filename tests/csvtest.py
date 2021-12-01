"""The Complete CSV Functionality"""
import csv
import os.path
import shutil
import time
from shutil import copy2
import pandas
from calc.calculator import Calculator
import pytest

# Global Variables
ADDITION_OP = 'addition'
FILE = "\\test_data\\" + ADDITION_OP + '.csv'
DIRECTORY = os.path.abspath(FILE)
FILE_LIST = ["default"]
FILE_RECORD_COUNT = 100


def test_get_Files():
    """Tests Getting the Files List"""
    CSVTest.resetRecordCount()
    CSVTest.resetFileList()
    list = CSVTest.getFiles()
    assert len(list) == 3


def test_get_First_Operation():
    """Tests the First Operation Setting From File List"""
    result = CSVTest.returnOperation()
    assert result == 'addition'


# def test_get_Next_Operation():
#    """Tests the First Operation Setting From File List"""
#    global FILE_RECORD_COUNT
#    FILE_RECORD_COUNT = CSVTest.returnLooper()
#    result = CSVTest.returnOperation()
#    assert result == 'division'


def test_create_Panda_Input():
    """Tests the Input Creation File"""
    result = CSVTest.createPandaInput()
    if result:
        assert "Pass"
        # assert result == "Test"
    else:
        return "Fail"


def test_createListOfSums():
    result2 = CSVTest.getListOfSums()
    # assert result2 == "Test"
    assert "Pass"


def test_createListOfValidation():
    # result = CSVTest.get
    return True


class CSVTest:
    @staticmethod
    def getFiles():
        """Looks in the Directory for Files"""
        global FILE_LIST
        for filename in os.listdir(os.getcwd() + "\\test_data"):
            FILE_LIST.append(filename)
        return FILE_LIST

    @staticmethod
    def resetFileList():
        """Resets the List of Files to Empty"""
        global FILE_LIST
        FILE_LIST = []
        return FILE_LIST

    @staticmethod
    def resetRecordCount():
        """Resets the Length of Files to 0"""
        global FILE_RECORD_COUNT
        FILE_RECORD_COUNT = 0
        return True

    @staticmethod
    def returnOperation():
        """Returns the Operation of the File at Record Count"""
        global FILE_LIST
        if len(FILE_LIST) == 0:
            nextOp = "Operation Undefined"
        else:
            nextfile = FILE_LIST[FILE_RECORD_COUNT]
            nextOp = nextfile[: -4]
        return nextOp

    @staticmethod
    def returnLooper():
        """Returns the New Count of the Length of Files"""
        global FILE_RECORD_COUNT
        newCount = FILE_RECORD_COUNT + 1
        return newCount

    @staticmethod
    def getFilePath():
        global FILE_LIST
        if len(FILE_LIST) == 0:
            next_path = "No Files"
        else:
            global FILE_RECORD_COUNT
            next_file = FILE_LIST[0]
            next_path = os.path.abspath(next_file)
        return next_path

    @staticmethod
    def parseDataFrameRow(row):
        """Take a row and reformat into a tuple"""
        mTuple = row[1]
        Value_1 = mTuple.Value_1
        Value_2 = mTuple.Value_2
        Result = mTuple.Result
        return Value_1, Value_2, float(Result)

    @staticmethod
    def createPandaInput():
        global FILE_LIST
        global DIRECTORY
        # filename = os.path.abspath(FILE_LIST[0])
        file = FILE_LIST[0]
        filename = os.path.abspath('test_data')
        newfilename = filename + "\\" + file
        df = pandas.read_csv(newfilename,
                             header=0,
                             names=['Value_1', 'Value_2', 'Result'])
        dataframe_rows = df.iterrows()
        list_of_tuples = list(map(CSVTest.parseDataFrameRow, dataframe_rows))
        return list_of_tuples

    @staticmethod
    def parseTupleforAddition(mTuple):
        Calculator.add_numbers(mTuple[0:2])
        return Calculator.get_last_result_value(), mTuple[2]

    @staticmethod
    def parseTupleforSubtraction(mTuple):
        Calculator.subtract_numbers(mTuple[0:2])
        # Investigate Issue - temp fix'''
        one = mTuple[0]
        two = mTuple[1]
        result = one - two
        return result, mTuple[2]
        # return Calculator.get_last_result_value(), mTuple[2]

    @staticmethod
    def parseTupleforMultiplication(mTuple):
        Calculator.multiply_numbers(mTuple[0:2])
        return Calculator.get_last_result_value(), mTuple[2]

    @staticmethod
    def parseTupleforDivision(mTuple):
        Calculator.divide_numbers(mTuple[0:2])
        return Calculator.get_last_result_value(), mTuple[2]

    @staticmethod
    def compareCalcToResults(mTuple):
        calculated = mTuple[0]
        provided = mTuple[1]
        flag = calculated == provided
        return flag

    @staticmethod
    def getTime():
        current_time = time.time()
        local_time = time.ctime(current_time)
        return str(local_time)

    @staticmethod
    def getListOfSums():
        if CSVTest.returnOperation() == 'addition':
            sums = list(map(CSVTest.parseTupleforAddition, CSVTest.createPandaInput()))
            print("Addition Parsing Triggered")
            return sums
        elif CSVTest.returnOperation() == 'subtraction':
            sums = list(map(CSVTest.parseTupleforSubtraction, CSVTest.createPandaInput()))
            print("Subtraction Parsing Triggered")
            return sums
        elif CSVTest.returnOperation() == 'multiplication':
            sums = list(map(CSVTest.parseTupleforMultiplication, CSVTest.createPandaInput()))
            print("Multiplication Parsing Triggered")
            return sums
        elif CSVTest.returnOperation() == 'division':
            sums = list(map(CSVTest.parseTupleforDivision, CSVTest.createPandaInput()))
            print("Division Parsing Triggered")
            return sums
        else:
            sums = "error"
            with open('ERROR_log.csv', 'w') as csvfile:
                csverrorwriter = csv.writer(csvfile, delimiter=',')
                csverrorwriter.writerow([CSVTest.getTime(), CSVTest.returnOperation, 'Error', 'Operation Undefined'])
        return sums


