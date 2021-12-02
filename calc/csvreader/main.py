"""The Complete CSV Methods"""
import csv
import os.path
import shutil
import time
from shutil import copy2
import pandas
from calc.calculator import Calculator

# '''Change the op to addition, subtraction, multiplication, or division'''
# op = 'division'
#
# '''Do not change'''
# file = op + '.csv'
# filename = os.path.abspath(file)
# donefile = op + '.csv'
# done = os.path.abspath(donefile)
# df = pandas.read_csv(filename,
#                      header=0,
#                      names=['Value_1', 'Value_2', 'Result'])
# dateframe_rows = df.iterrows()
#
# print("Beginning CSV Test")
#
#
# def parseDataFrameRow(row):
#     """Take a row and reformat into a tuple"""
#     mTuple = row[1]
#     Value_1 = mTuple.Value_1
#     Value_2 = mTuple.Value_2
#     Result = mTuple.Result
#     return Value_1, Value_2, float(Result)
#
#
# def parseTupleforAddition(mTuple):
#     Calculator.add_numbers(mTuple[0:2])
#     return Calculator.get_last_result_value(), mTuple[2]
#
#
# def parseTupleforSubtraction(mTuple):
#     Calculator.subtract_numbers(mTuple[0:2])
#     '''Investigate Issue - temp fix'''
#     one = mTuple[0]
#     two = mTuple[1]
#     result = one - two
#     return result, mTuple[2]
#     '''return Calculator.get_last_result_value(), mTuple[2]'''
#
#
# def parseTupleforMultiplication(mTuple):
#     Calculator.multiply_numbers(mTuple[0:2])
#     return Calculator.get_last_result_value(), mTuple[2]
#
#
# def parseTupleforDivision(mTuple):
#     Calculator.divide_numbers(mTuple[0:2])
#     return Calculator.get_last_result_value(), mTuple[2]
#
#
# def compareCalcToResults(mTuple):
#     calculated = mTuple[0]
#     provided = mTuple[1]
#     flag = calculated == provided
#     return flag
#
#
# def getTime():
#     current_time = time.time()
#     local_time = time.ctime(current_time)
#     return str(local_time)
#
#
# def resetRecordCount():
#     return 0
#
#
# def addRecord(current):
#     new_count = current + 1
#     return new_count
#
#
# def setOperation():
#     op = file[: -4]
#     return op
#
#
# print('Operation set: ' + setOperation())
#
# list_of_tuples = list(map(parseDataFrameRow, dateframe_rows))
#
# if op == 'addition':
#     list_of_sums = list(map(parseTupleforAddition, list_of_tuples))
#     print("Addition Parsing Triggered")
# if op == 'subtraction':
#     list_of_sums = list(map(parseTupleforSubtraction, list_of_tuples))
#     print("Subtraction Parsing Triggered")
# elif op == 'multiplication':
#     list_of_sums = list(map(parseTupleforMultiplication, list_of_tuples))
#     print("Multiplication Parsing Triggered")
# elif op == 'division':
#     list_of_sums = list(map(parseTupleforDivision, list_of_tuples))
#     print("Division Parsing Triggered")
# else:
#     list_of_sums = "error"
#     with open('ERROR_log.csv', 'w') as csvfile:
#         csverrorwriter = csv.writer(csvfile, delimiter=',')
#         csverrorwriter.writerow([getTime(), op, 'Error', 'Operation Undefined'])
#
# list_of_validation = list(map(compareCalcToResults, list_of_sums))
#
# print()
# print("Here are the lists of tuples created")
# print(list_of_tuples)
# print(list_of_sums)
# print(list_of_validation)
# print(getTime())
#
# resetRecordCount()
#
# with open('result_log2.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',')
#     csvwriter.writerow(['Timestamp', 'FileName', 'RecordNumber',
#     'Operation', 'CalcResult', 'Flag'])
#     for i in range(len(df)):
#         a, b = list_of_sums[i]
#         if a != 'ZeroDivisionError':
#             csvwriter.writerow([getTime(), file, addRecord(i),
#             setOperation(), a, list_of_validation[i]])
#         elif a == 'ZeroDivisionError':
#             csvwriter.writerow([getTime(), file, addRecord(i),
#             setOperation(), a, 'ZeroDivisionError'])
#             error_row = ([getTime(), op, 'Error', 'Error Triggered'])
#             with open('ERROR_log.csv', 'a') as f:
#                 csverrorwriter = csv.writer(f, delimiter=',')
#                 csverrorwriter.writerow([error_row])
#
#         else:
#             csvwriter.writerow(["Done"])
#
# shutil.move(filename, done, copy_function=copy2)

# Global Variables
ADDITION_OP = 'addition'
FILE = "\\test_data\\" + ADDITION_OP + '.csv'
DIRECTORY = os.path.abspath(FILE)
FILE_LIST = ["default"]
FILE_RECORD_COUNT = 100
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
    def createTuple():
        processed_list = CSVTest.getTuples(CSVTest.doIterration(CSVTest.createPandaDF()))
        return processed_list

    @staticmethod
    def createPandaDF():
        global FILE_LIST
        global DIRECTORY
        # filename = os.path.abspath(FILE_LIST[0])
        file = FILE_LIST[0]
        filename = os.path.abspath('test_data')
        newfilename = filename + "\\" + file
        df = pandas.read_csv(newfilename,
                             header=0,
                             names=['Value_1', 'Value_2', 'Result'])
        return df

    @staticmethod
    def doIterration(df):
        """Creates the Dataframe Rows from DF"""
        dataframe_rows = df.iterrows()
        return dataframe_rows

    @staticmethod
    def getTuples(dataframe_rows):
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
            sums = list(map(CSVTest.parseTupleforAddition, CSVTest.createTuple()))
            print("Addition Parsing Triggered")
            return sums
        elif CSVTest.returnOperation() == 'subtraction':
            sums = list(map(CSVTest.parseTupleforSubtraction, CSVTest.createTuple()))
            print("Subtraction Parsing Triggered")
            return sums
        elif CSVTest.returnOperation() == 'multiplication':
            sums = list(map(CSVTest.parseTupleforMultiplication, CSVTest.createTuple()))
            print("Multiplication Parsing Triggered")
            return sums
        elif CSVTest.returnOperation() == 'division':
            sums = list(map(CSVTest.parseTupleforDivision, CSVTest.createTuple()))
            print("Division Parsing Triggered")
            return sums
        else:
            sums = "error"
            with open('ERROR_log.csv', 'w') as csvfile:
                csverrorwriter = csv.writer(csvfile, delimiter=',')
                csverrorwriter.writerow([CSVTest.getTime(), CSVTest.returnOperation, 'Operation Undefined'])
        return sums

    @staticmethod
    def getValidation():
        """Gets List of Validation for Calculations"""
        validation = list(map(CSVTest.compareCalcToResults, CSVTest.getListOfSums()))
        return validation

    @staticmethod
    def addRecord(current):
        new_count = current + 1
        return new_count

    @staticmethod
    def writeToLog():
        with open(os.path.abspath('result_log2.csv'), 'w') as csvfile:
            global FILE_LIST
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(['Timestamp', 'FileName', 'Record #', 'Operation', 'CalcResult', 'Flag'])
            loop_count = len(CSVTest.createPandaDF())
            for i in range(loop_count):
                # range(len(CSVTest.createPandaDF())):
                a, b = CSVTest.getListOfSums()[i]
                if a != 'ZeroDivisionError':
                    csvwriter.writerow(
                        [CSVTest.getTime(), FILE_LIST[i - 1], CSVTest.addRecord(i),
                         CSVTest.returnOperation(), a, CSVTest.getValidation()[i]])
                elif a == 'ZeroDivisionError':
                    csvwriter.writerow(
                        [CSVTest.getTime(), FILE_LIST[i - 1], CSVTest.addRecord(i), CSVTest.returnOperation(), a,
                         'ZeroDivisionError'])
                    error_row = ([CSVTest.getTime(), CSVTest.returnOperation(), 'Error', 'Error Triggered'])
                    with open('ERROR_log.csv', 'a') as f:
                        csverrorwriter = csv.writer(f, delimiter=',')
                        csverrorwriter.writerow([error_row])

                else:
                    csvwriter.writerow(["Done"])

            return "Successfully Written"

    @staticmethod
    def moveToDone():
        """This method moves files to the done folder"""
        shutil.move(FILE, os.path.abspath(FILE_LIST[FILE_RECORD_COUNT]), copy_function=copy2)
        return 'True'

