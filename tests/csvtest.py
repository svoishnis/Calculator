"""Testing the CSV Methods"""
import pytest

from calc.csvreader.main import getAbbPath

@pytest.fixture
def test_csv_get_abb_path():
    """Test for getting the absolute path"""
    file = 'addition_test.py'
    filename = getAbbPath(file)
    return filename
def test_read_File():

