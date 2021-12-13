import os

import pandas as pd
from csvmanager.absolutePath import absolutepath
in_file = "tests/test_data/input.csv"

class Read:
    @staticmethod
    def DataFrameFromCSVFile():
        return pd.read_csv(absolutepath(in_file))