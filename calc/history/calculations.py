"""Calculation history Class"""
class Calculations:
    """Calculation class"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """The method to clear history"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """The method to find the number of history items"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """Gets the last calculation from the history"""
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        """Gets the first calculation from the hsitory"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
