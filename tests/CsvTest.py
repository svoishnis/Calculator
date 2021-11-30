from calc.CSVReader.main import getAbbPath


@pytest.fixture
def test_csv_get_abb_path():
    file = 'addition_test.py'
    filename = getAbbPath(file)
    return filename
