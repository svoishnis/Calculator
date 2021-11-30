import csv
import os.path
import time
import pandas as pandas

from calc.calculator import Calculator


class CSVMethods:
    file = 'addition.csv'

    @staticmethod
    def getAbbPath(file):
        """Gets the Entire File Path"""
        filename = os.path.abspath(file)
        return filename

    @staticmethod
    def readFile(file):
        """Reads a File Provided Using Pandas and Creates a Structure"""
        df = pandas.read_csv(CSVMethods.getAbbPath(file),
                             header=0,
                             names=['Value_1', 'Value_2', 'Result'])
        return df

    '''def iterateFile(df):
        """Iterates through a dataframe"""
        dateframe_rows = df.iterrows()
        return dateframe_rows

    def createTuples(dateframe_rows):
        """Creates the Tuples for Other Methods"""
        list_of_tuples = list(map(parseDataFrameRow, dateframe_rows))
        return list_of_tuples

    def createSums(list_of_tuples):
        list_of_sums = list(map(parseTupleforAddition, list_of_tuples))
        return list_of_sums

    def createValidations(list_of_sums):
        list_of_validation = list(map(compareCalcToResults, list_of_sums))
        return list_of_validation

    def parseDataFrameRow(row):
        mTuple = row[1]
        Value_1 = mTuple.Value_1
        Value_2 = mTuple.Value_2
        Result = mTuple.Result
        return (Value_1, Value_2, float(Result))

    def parseTupleforAddition(mTuple):
        Calculator.add_numbers(mTuple[0:2])
        return (Calculator.get_last_result_value(), mTuple[2])

    def parseTupleforSubtraction(mTuple):
        Calculator.subtract_numbers(mTuple[0:2])
        return (Calculator.get_last_result_value(), mTuple[2])

    def parseTupleforMultiplication(mTuple):
        Calculator.multiply_numbers(mTuple[0:2])
        return (Calculator.get_last_result_value(), mTuple[2])

    def parseTupleforDivision(mTuple):
        Calculator.divide_numbers(mTuple[0:2])
        return (Calculator.get_last_result_value(), mTuple[2])

    def compareCalcToResults(mTuple):
        calculated = mTuple[0]
        provided = mTuple[1]
        flag = calculated == provided
        return flag

    def getCurrentTime():
        current_time = time.time()
        local_time = time.ctime(current_time)
        return str(local_time)

    def resetRecordCount():
        return 0

    def addRecord(current):
        new_count = current + 1
        return new_count

    def setOperation(file):
        if file == 'addition.csv':
            operation = 'Addition'
        if file == 'substraction.csv':
            operation = 'Subtraction'
        if file == 'multiplication.csv':
            operation = 'Multiplication'
        if file == 'division.csv':
            operation = 'Division'
        return operation

    """with open('result_log2.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Timestamp', 'FileName', 'Record Number', 'Operation', 'Result'])
        for i in df.iterrows():
            csvwriter.writerow([getCurrentTime(), file, addRecord(resetRecordCount()),setOperation(file), Calculator.get_last_result_value() ])
            print()
    print(df)"""'''
