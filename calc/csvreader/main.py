import csv
import os.path
import shutil
import time
from shutil import copy2

import pandas as pandas
from calc.calculator import Calculator

'''Change the op to addition, subtraction, multiplication, or division'''
op = 'division'

'''Do not change'''
file = op + '.csv'
filename = os.path.abspath(file)
donefile = 'done\\' + op + '.csv'
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
    Calculator.add_numbers(mTuple[0:2])
    return Calculator.get_last_result_value(), mTuple[2]


def parseTupleforSubtraction(mTuple):
    Calculator.subtract_numbers(mTuple[0:2])
    '''Investigate Issue - temp fix'''
    one = mTuple[0]
    two = mTuple[1]
    result = one - two
    return result, mTuple[2]
    '''return Calculator.get_last_result_value(), mTuple[2]'''


def parseTupleforMultiplication(mTuple):
    Calculator.multiply_numbers(mTuple[0:2])
    return Calculator.get_last_result_value(), mTuple[2]


def parseTupleforDivision(mTuple):
    Calculator.divide_numbers(mTuple[0:2])
    return Calculator.get_last_result_value(), mTuple[2]


def compareCalcToResults(mTuple):
    calculated = mTuple[0]
    provided = mTuple[1]
    flag = calculated == provided
    return flag


def getTime():
    current_time = time.time()
    local_time = time.ctime(current_time)
    return str(local_time)


def resetRecordCount():
    return 0


def addRecord(current):
    new_count = current + 1
    return new_count


def setOperation():
    op = file[: -4]
    return op


print('Operation set: ' + setOperation())

list_of_tuples = list(map(parseDataFrameRow, dateframe_rows))

if op == 'addition':
    list_of_sums = list(map(parseTupleforAddition, list_of_tuples))
    print("Addition Parsing Triggered")
if op == 'subtraction':
    list_of_sums = list(map(parseTupleforSubtraction, list_of_tuples))
    print("Subtraction Parsing Triggered")
elif op == 'multiplication':
    list_of_sums = list(map(parseTupleforMultiplication, list_of_tuples))
    print("Multiplication Parsing Triggered")
elif op == 'division':
    list_of_sums = list(map(parseTupleforDivision, list_of_tuples))
    print("Division Parsing Triggered")
else:
    list_of_sums = "error"
    with open('ERROR_log.csv', 'w') as csvfile:
        csverrorwriter = csv.writer(csvfile, delimiter=',')
        csverrorwriter.writerow([getTime(), op, 'Error', 'Operation Undefined'])

list_of_validation = list(map(compareCalcToResults, list_of_sums))

print()
print("Here are the lists of tuples created")
print(list_of_tuples)
print(list_of_sums)
print(list_of_validation)
print(getTime())

resetRecordCount()

with open('result_log2.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Timestamp', 'FileName', 'RecordNumber', 'Operation', 'CalcResult', 'Flag'])
    for i in range(len(df)):
        a, b = list_of_sums[i]
        if a != 'ZeroDivisionError':
            csvwriter.writerow([getTime(), file, addRecord(i), setOperation(), a, list_of_validation[i]])
        elif a == 'ZeroDivisionError':
            csvwriter.writerow([getTime(), file, addRecord(i), setOperation(), a, 'ZeroDivisionError'])
            error_row = ([getTime(), op, 'Error', 'Error Triggered'])
            with open('ERROR_log.csv', 'a') as f:
                csverrorwriter = csv.writer(f, delimiter=',')
                csverrorwriter.writerow([error_row])

        else:
            csvwriter.writerow(["Done"])

shutil.move(filename, done, copy_function=copy2)
