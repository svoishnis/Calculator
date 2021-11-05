import unittest
from src.Stats.Stats import Stats
import random
from src.SupportFunctions.getRandomSeeded import get_random_int_list

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.stats = Stats()
        random.seed(1000)
        self.testData = random.randint(0,10)
        self.random_lst = get_random_int_list()
        self.test_lst = [1,2,3]

    def test_calculator_instance(self):
        self.assertIsInstance(self.stats, Stats)
        print("Completed Statistic Calculator Instance Test")

    def test_calculator_result(self):
        self.assertEqual(self.calculator.result, 0)
        print("Stats Calculator Result Test Completed")

    if __name__ == '__main__':
        unittest.main()