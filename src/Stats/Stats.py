from src.calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader
from src.Stats.Mean import mean
from src.Stats.SampleMean import sample_mean
from src.Stats.Median import median
from src.Stats.Mode import mode
from src.Stats.PopVariance import population_variance
from src.Stats.StandardDeviation import std

class Stats(Calculator):
    data = []

    def init(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self, data):
        self.data = mean(data)
        return self.data

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self,data):
        self.result = mode(data)
        return self.result

    def pop_variance(self, data):
        self.result = population_variance(data)
        return self.result

    def std(self, data):
        self.result = std(data)
        return self.result
