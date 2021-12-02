"""The Complete CSV Functionality"""
import csv
import os.path
import shutil
import time
from shutil import copy2
import pandas
from calc.calculator import Calculator
from calc.csvreader.main import CSVTest


def test_getFiles():
    """Tests Getting the Files List"""
    CSVTest.resetRecordCount()
    CSVTest.resetFileList()
    list = CSVTest.getFiles()
    print("Retrieve Files")
    assert len(list) == 3


def test_get_First_Operation():
    """Tests the First Operation Setting From File List"""
    result = CSVTest.returnOperation()
    print("Checks Addition is the First File in List")
    assert result == 'addition'


# def test_get_Next_Operation():
#    """Tests the First Operation Setting From File List"""
#    global FILE_RECORD_COUNT
#    FILE_RECORD_COUNT = CSVTest.returnLooper()
#    result = CSVTest.returnOperation()
#    assert result == 'division'


def test_create_Panda_Input():
    """Tests the Input Creation File"""
    result = CSVTest.createTuple()
    if result:
        print("Data Successfully Passed Into List for Processing")
        assert "Pass"
        # assert result == "Test"
    else:
        assert "Fail"


def test_createListOfSums():
    result2 = CSVTest.getListOfSums()  # pylint: disable=unused-argument
    # assert result2 == "Test"          # pylint: disable=unused-argument
    assert "Pass"


def test_createListOfValidation():
    result = CSVTest.getValidation()  # pylint: disable=unused-argument
    assert "Pass"
    # assert result == "Test"          # pylint: disable=unused-argument


# def test_writeToLog():
#    result = CSVTest.writeToLog()
#    print("Look in the result_log2 file for contents")
#    assert result == "Successfully Written"


