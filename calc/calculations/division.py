"""Division class"""
import pprint
from calc.calculations.calculation import Calculation



class Division(Calculation):

    """Division calculation object"""
    def get_result(self):
        """get the division results"""
        initial = 1.0
        result = 0
        for value in self.values:
            pprint.pprint(value)
            if result==0:
                result = value / initial
            else:
                try:
                    result = result / value
                except ZeroDivisionError:
                    return 0.0
            pprint.pprint(result)
        return result
