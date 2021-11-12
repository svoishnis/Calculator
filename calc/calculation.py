
"""This is our calculation Abstract Class"""
class Calculation: #pylint: disable=too-few-public-methods
    """Subclassed by Addition"""
    #contstructor
    def __init__(self,value_a, value_b):
        #self references the instantiated object of the class
        #these are instance properties - shared with the child classes (add, sub, etc.)
        self.value_a = value_a
        self.value_b = value_b

    # Class Factory Method <- bound to the class and not the instance of the class
    @classmethod
    def create(cls, value_a, value_b):
        """Test"""
        return cls(value_a,value_b)
