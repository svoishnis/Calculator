"""Testing the Calculator"""

import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader

class UnitTest(unittest.TestCase): #Test Driven Development - testing code works
    def setUp(self) -> None:
        self.calculator = Calculator() #Initialize Calculator in each unit test

    def test_calculator_instance(self):
        self.assertIsInstance(self.calculator, Calculator) #Test Existence of Calculator
        print("Calculator Instance Test Completed")

    def test_calculator_result(self):
        self.assertEqual(self.calculator.result,0)
        print("Calculator Result Test Completed")

    def test_calculator_addition(self):
        print("Addition Test:")
        test_data_addition = CsvReader('src/Tests/UnitTestData/UnitTest_Addition.csv').data
        for row in test_data_addition:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']),int(row['Result']))
        print("Addition Test Complete")

if __name__ == '__main__':
    unittest.main()