"""Calculation history Class"""
class Calculations:
    """Create a storage for calculation history"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clears history of calculations"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """Method returns the amount of calculations stored"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """Returns the most recent calculation stored"""
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        """Returns the oldest calculation stored"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """Returns a specific calculation stored"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ Add a specific calculation to the history"""
        return Calculations.history.append(calculation)
