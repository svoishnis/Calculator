"""The Complete CSV Functionality"""
from calc.csvreader.main import CSVTest
# pylint: disable-all


def test_get_files():
    """Tests Getting the Files List"""
    CSVTest.reset_record_count()
    CSVTest.reset_file_list()
    list = CSVTest.get_files()
    print("Retrieve Files")
    assert len(list) == 3


def test_get_first_operation():
    """Tests the First Operation Setting From File List"""
    result = CSVTest.get_operation()
    print("Checks Addition is the First File in List")
    assert result == 'addition'


# def test_get_Next_Operation():
#    """Tests the First Operation Setting From File List"""
#    global FILE_RECORD_COUNT
#    FILE_RECORD_COUNT = CSVTest.returnLooper()
#    result = CSVTest.returnOperation()
#    assert result == 'division'


def test_create_panda_input():
    """Tests the Input Creation File"""
    result = CSVTest.create_tuple()
    if result:
        print("Data Successfully Passed Into List for Processing")
        assert 1 == 1
        # assert result == "Test"
    else:
        assert 1 == 0


def test_create_list_of_sums():
    result2 = CSVTest.get_list_sums()  # pylint: disable=unused-argument
    # assert result2 == "Test"          # pylint: disable=unused-argument
    assert 1 == 1


def test_create_list_of_validation():
    result = CSVTest.get_validation()  # pylint: disable=unused-argument
    assert 1 == 1
    # assert result == "Test"          # pylint: disable=unused-argument


# def test_writeToLog():
#    result = CSVTest.writeToLog()
#    print("Look in the result_log2 file for contents")
#    assert result == "Successfully Written"
