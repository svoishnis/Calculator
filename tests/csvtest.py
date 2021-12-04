"""The Complete CSV Functionality"""

from calc.csvreader.main import CSVTest


# pylint: disable-all

def test_get_file_looper():
    """Tests Getting the File Looper Variable"""
    looper = CSVTest.get_file_looper()
    print("File List Looper retrieved")
    assert looper == 500


def test_reset_file_looper():
    """Tests resetting the file looper"""
    looper = CSVTest.rest_file_looper()
    print("File List Looper reset")
    assert looper == 0


def test_loop_files():
    """Test the setting of the File Looper"""
    CSVTest.loop_files()
    CSVTest.loop_files()
    looper = CSVTest.get_file_looper()
    assert looper == 2


def test_get_file_name():
    """Tests the retrieval of file name variable"""
    name = CSVTest.get_file_name()
    print("Get file name helper")
    assert name == "Default File Name"


def test_reset_file_list():
    """Tests the helper to reset the global file list"""
    list = CSVTest.reset_file_list()
    print("File list emptied")
    assert list == []


def test_reset_file_count():
    CSVTest.get_files()
    CSVTest.reset_record_count()
    count = CSVTest.get_record_count()
    print("Test reset and get methods for the count of Files")
    assert count == 0


def test_set_record_count():
    """Tests helper for setting the file count"""
    CSVTest.get_files()
    count = CSVTest.get_record_count()
    print("Getting Files sets the record count automatically")
    assert count == 3


def test_get_file_list():
    """Test Getting the Files List"""
    list = CSVTest.get_file_list()
    print("Retrieving global file List. First File in list " + list[0])
    assert len(list) == 3


def test_get_operation():
    """Tests the First Operation Setting From File List"""
    CSVTest.reset_parameters()
    result = CSVTest.get_operation()
    print("Checks getting the default operation")
    assert result == 'Default Operation'


def test_set_operation_no_files():
    """Tests the helper for setting the operation"""
    CSVTest.reset_record_count()
    result = CSVTest.set_operation()
    print(CSVTest.get_record_count())
    assert result == "No Files: Operation Undefined"  # "Default List Value"


def test_set_operation_file_in_list():
    """Test condition of helper for setting the operation"""
    CSVTest.get_files()
    result = CSVTest.set_operation()
    print(CSVTest.get_record_count())
    assert result == "addition"


def test_get_next_operation():
    """Tests the First Operation Setting From File List"""
    CSVTest.get_files()
    CSVTest.loop_files()
    result = CSVTest.set_operation()
    print(CSVTest.get_record_count())
    assert result == 'division'


def test_create_panda_input():
    """Tests the Input Creation File"""
    data_frame = CSVTest.create_panda_df()
    print("Data Frame Created: \n")
    print(data_frame)


def test_do_iteration():
    """Tests the Iteration and Create a Tuple of Rows"""
    dataframe_rows = CSVTest.do_iteration(CSVTest.create_panda_df())
    print("Tuple of Rows Created: \n")
    print(dataframe_rows)


def test_get_data_frame_rows():
    """Tests getting the dataframe rows"""
    dataframe_rows = CSVTest.get_data_frame_rows()
    print("Get the data frame: \n")
    print(dataframe_rows)


def test_create_list_of_tuples():
    """Tests the parse helper dataframe rows"""
    result = CSVTest.create_tuple()
    print("Create List of Tuples: \n")
    print(result)
    assert result == [(1, 2, -1.0), (2, 3, -1.0),
                      (3, 4, -1.0), (4, 5, -1.0),
                      (5, 6, -1.0), (6, 7, -1.0),
                      (7, 8, -1.0), (8, 9, -1.0),
                      (9, 10, 19.0), (10, 11, 21.0),
                      (11, 12, 23.0), (12, 13, 25.0),
                      (13, 14, 27.0), (0, 0, 0.0),
                      (5, 0, 0.0), (3, 4, 6.0)]


def test_create_list_of_calculations():
    """Tests the creation of a list of Calculations
    and Provided Results"""
    CSVTest.get_files()
    calculations = CSVTest.create_list_calculations()  # pylint: disable=unused-argument
    print("List of Calculations: \n")
    print(calculations)
    assert calculations == [(3.0, 3.0), (5.0, 5.0), (7.0, 7.0),
                            (9.0, 9.0), (11.0, 11.0), (13.0, 13.0),
                            (15.0, 15.0), (17.0, 17.0), (19.0, 19.0),
                            (21.0, 21.0), (23.0, 23.0), (25.0, 25.0),
                            (27.0, 27.0), (3.0, 400.0)]  # pylint: disable=unused-argument#


def test_create_list_of_validation():
    """Creates a list of validations on Calculated vs. Results"""
    result = CSVTest.get_validation()  # pylint: disable=unused-argument
    print("Create a list of Validations: \n")
    print(result)
    assert result == [True,
                      True,
                      True,
                      True,
                      True,
                      True,
                      True,
                      True,
                      True,
                      True,
                      True,
                      True,
                      True,
                      False]  # pylint: disable=unused-argument


def test_write_to_log():
    """Tests the Writing to a Log Function"""
    result = CSVTest.write_to_log()
    print("Look in the result_log2 file for contents")
    assert result == "Successfully Written"


def test_quick_write_log():
    """This tests the full Logic of Validation in one shot"""
    print("This is the Quick Test")
    CSVTest.get_files()
    CSVTest.create_list_calculations()
    CSVTest.get_validation()
    result = CSVTest.write_to_log()
    print(result)
    assert result == "Successfully Written"


def test_move_to_done():
    """Tests the functionality of moving the tested file to done"""
    CSVTest.set_operation()
    result = CSVTest.move_to_done()
    print("Look in the done folder for contents \n")
    # assert result == "Moved to Done"
    """Currently hard coded need to fix path calls"""
