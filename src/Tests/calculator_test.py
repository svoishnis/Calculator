"""Testing the Calculator"""
import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader


class UnitTest(unittest.TestCase):  # Test Driven Development - testing code works
    def setUp(self) -> None:
        self.calculator = Calculator()  # Initialize Calculator in each unit test

    def test_calculator_instance(self):
        self.assertIsInstance(self.calculator, Calculator)  # Test Existence of Calculator
        print("Calculator Instance Test Completed")

    def test_calculator_result(self):
        self.assertEqual(self.calculator.result, 0)
        print("Calculator Result Test Completed")

    def test_add_method_calculator(self):
        print("Beginning Addition Test")
        test_data_add = CsvReader('Tests/UnitTestData/Unit Test Addition.csv').data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Completed Addition Test")

    def test_subtract_method_calculator(self):
        print("Beginning Subtraction Test")
        test_data_subtract = CsvReader('src/Tests/UnitTestData/Unit Test Subtraction.csv').data
        for row in test_data_subtract:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Completed Subtraction Test")

    def test_multiplication_method_calculator(self):
        print("Beginning Multiplication Test")
        test_data_multiply = CsvReader('src/Tests/UnitTestData/Unit Test Multiplication.csv').data
        for row in test_data_multiply:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
        print("Completed Multiplication Test")

    def test_division_method_calculator(self):
        print("Beginning Division Test")
        test_data_divide = CsvReader('src/Tests/UnitTestData/Unit Test Division.csv').data
        for row in test_data_divide:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
        print("Completed Division Test")

    def test_division_method_calculator_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(0, 1)

    def test_square_method_calculator(self):
        print("Beginning Square Test")
        test_data_square = CsvReader('src/Tests/UnitTestData/Unit Test Square.csv').data
        for row in test_data_square:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
        print("Completed Square Test")

    def test_sqrt_method_calculator(self):
        print("Beginning Square Root Test")
        test_data_sqrt = CsvReader('src/Tests/UnitTestData/Unit Test Square Root.csv').data
        for row in test_data_sqrt:
            self.assertAlmostEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
        print("Completed Square Root Test")

    def test_sqrt_negatives_method_calculator(self):
        with self.assertRaises(ValueError):
            self.calculator.sqrt(-25)


if __name__ == '__main__':
    unittest.main()
