"""The Complete CSV Functionality"""
import csv
import os.path
import shutil
import time
from shutil import copy2
import pandas
from calc.calculator import Calculator
import pytest

"""Global Variables"""
ADDITION_OP = 'addition'
file = ADDITION_OP + '.csv'
DIRECTORY = os.path.abspath(file)
FILE_LIST = ["default"]
FILE_RECORD_COUNT = 100


def test_getFiles():
    """Tests Getting the Files List"""
    CSVTest.resetRecordCount()
    CSVTest.resetFileList()
    return CSVTest.getFiles()


def test_getFirstOperation():
    """Tests the First Operation Setting From File List"""
    result = CSVTest.returnOperation()
    assert result == 'addition'

def test_getFilePath():
    """Gets the FilePath of the Current Record"""
    path = CSVTest.getFilePath()
    assert path == "C:\\Users\\svois\\PycharmProjects\\calc2\\tests\\addition.csv"


def test_getNextOperation():
    """Tests the First Operation Setting From File List"""
    global FILE_RECORD_COUNT
    FILE_RECORD_COUNT = CSVTest.returnLooper()
    result = CSVTest.returnOperation()
    assert result == 'division'

def test_getFilePath():
    """Gets the FilePath of the Current Record"""
    path = CSVTest.getFilePath()
    assert path == "C:\\Users\\svois\\PycharmProjects\\calc2\\tests\\division.csv"


class CSVTest:
    @staticmethod
    def getFiles():
        """Looks in the Directory for Files"""
        global FILE_LIST
        for filename in os.listdir("test_data"):
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
    def returnLooper():
        """Returns the New Count of the Length of Files"""
        global FILE_RECORD_COUNT
        newCount = FILE_RECORD_COUNT + 1
        return newCount

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
    def getFilePath():
        global FILE_LIST
        if len(FILE_LIST) == 0:
            path = "No Files"
        else:
            global FILE_RECORD_COUNT
            next_file = FILE_LIST[FILE_RECORD_COUNT]
            next_path = os.path.abspath(next_file)
        return next_path
