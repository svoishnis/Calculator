"""The Complete CSV Functionality"""
import csv
import os.path
import shutil
import time
from shutil import copy2
import pandas
from calc.calculator import Calculator

"""Change the op to addition, subtraction, multiplication, or division"""
Operation = 'division'

'''Do not change'''
file = Operation + '.csv'
filename = os.path.abspath(file)
donefile = 'done\\' + Operation + '.csv'
done = os.path.abspath(donefile)
df = pandas.read_csv(filename,
                     header=0,
                     names=['Value_1', 'Value_2', 'Result'])
dateframe_rows = df.iterrows()

print("Beginning CSV Test")


def parseDataFrameRow(row):
    """Take a row and reformat into a tuple"""
    mTuple = row[1]
    Value_1 = mTuple.Value_1
    Value_2 = mTuple.Value_2
    Result = mTuple.Result
    return Value_1, Value_2, float(Result)


def parseTupleforAddition(mTuple):
    """Parses the Tuple for the Addition Method"""
    Calculator.add_numbers(mTuple[0:2])
    return Calculator.get_last_result_value(), mTuple[2]


def parseTupleforSubtraction(mTuple):
    """Parses the Tuple for the Subtraction Method"""
    Calculator.subtract_numbers(mTuple[0:2])
    '''Investigate Issue - temp fix'''
    one = mTuple[0]
    two = mTuple[1]
    result = one - two
    return result, mTuple[2]
    # return Calculator.get_last_result_value(), mTuple[2]


def parseTupleforMultiplication(mTuple):
    """Parses the Tuple for the Multiplication Method"""
    Calculator.multiply_numbers(mTuple[0:2])
    return Calculator.get_last_result_value(), mTuple[2]


def parseTupleforDivision(mTuple):
    """Parses the Tuple for the Division Method"""
    Calculator.divide_numbers(mTuple[0:2])
    return Calculator.get_last_result_value(), mTuple[2]


def compareCalcToResults(mTuple):
    """Compares the Caclulated to the Provided Result"""
    calculated = mTuple[0]
    provided = mTuple[1]
    flag = calculated == provided
    return flag


def getTime():
    """Returns the Current Time in a Readable Format"""
    current_time = time.time()
    local_time = time.ctime(current_time)
    return str(local_time)


def resetRecordCount():
    """Resets the Record Count to Zero"""
    return 0


def addRecord(current):
    """Counter for the Number of Records Recorded"""
    new_count = current + 1
    return new_count


def setOp():
    """Sets the Operation Type"""
    return Operation


print('Operation set: ' + setOp())

List_of_tuples = list(map(parseDataFrameRow, dateframe_rows))

if Operation == 'addition':
    List_of_sums = list(map(parseTupleforAddition, List_of_tuples))
    print("Addition Parsing Triggered")
if Operation == 'subtraction':
    List_of_sums = list(map(parseTupleforSubtraction, List_of_tuples))
    print("Subtraction Parsing Triggered")
elif Operation == 'multiplication':
    List_of_sums = list(map(parseTupleforMultiplication, List_of_tuples))
    print("Multiplication Parsing Triggered")
elif Operation == 'division':
    List_of_sums = list(map(parseTupleforDivision, List_of_tuples))
    print("Division Parsing Triggered")
else:
    List_of_sums = "error"
    with open('ERROR_log.csv', 'w') as csvfile:
        csverrorwriter = csv.writer(csvfile, delimiter=',')
        csverrorwriter.writerow([getTime(), Operation, 'Error', 'Operation Undefined'])

List_of_validation = list(map(compareCalcToResults, List_of_sums))

print()
print("Here are the lists of tuples created")
print(List_of_tuples)
print(List_of_sums)
print(List_of_validation)
print(getTime())

resetRecordCount()

with open('result_log2.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Timestamp', 'FileName', 'RecordNumber', 'Operation', 'CalcResult', 'Flag'])
    for i in range(len(df)):
        a, b = List_of_sums[i]
        if a != 'ZeroDivisionError':
            csvwriter.writerow([getTime(), file, addRecord(i), setOp(), a, List_of_validation[i]])
        elif a == 'ZeroDivisionError':
            csvwriter.writerow([getTime(), file, addRecord(i), setOp(), a, 'ZeroDivisionError'])
            error_row = ([getTime(), Operation, 'Error', 'Error Triggered'])
            with open('ERROR_log.csv', 'a') as f:
                csverrorwriter = csv.writer(f, delimiter=',')
                csverrorwriter.writerow([error_row])

        else:
            csvwriter.writerow(["Done"])

shutil.move(filename, done, copy_function=copy2)
