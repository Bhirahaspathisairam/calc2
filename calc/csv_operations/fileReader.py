import os
import pandas as pd
from pathlib import Path
import shutil

class FileReader:
    """Class is built to read csv files"""
    @staticmethod
    def abs_path_to_csv(filepath):
        """Converts a relative path into an absolute path"""
        return (Path(filepath)).absolute()

    @staticmethod
    def csv_to_df(csv_to_convert):
        """Converts a csv file into a dataframe"""
        path = FileReader.abs_path_to_csv(csv_to_convert)
        return pd.read_csv(path)

    @staticmethod
    def search_csv(name_of_csv):
        """Searches for a particular csv in an input folder and returns location"""
        abs_location = "calc2/tests/input_csv/" + name_of_csv
        return abs_location

    @staticmethod
    def df_to_csv(df_to_convert: pd.DataFrame, file_name):
        """Converts a dataframe into a csv file"""
        df_to_convert.to_csv(file_name + ".csv", index=False)
        return True

    @staticmethod
    def set_directory():
        """Changes the directory to 'results' in order to commit the logs"""
        os.chdir('calc2/tests/results')
        return True

    @staticmethod
    def move_to_destination(current_csv_file,
                            destination='cal2/tests/csvs_for_operations/output_csv'):
        """Moves csv files from one folder to another"""
        shutil.move(current_csv_file, destination)

