"""Testing CSV Functions"""
import pandas
import os.path
from csvmanager.write import Write
from csvmanager.read import Read
import pandas as pd

def test_write_csv():
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = 'input.csv'
    path = 'tests/test_data'
    fullPath = path + '/' + filename
    name_dict = {
        'value_1': ['1'],
        'value_2': ['2'],
        'result': [3.0],
        'operation performed': "addition"
    }
    os.remove(fullPath)
    df = pd.DataFrame(name_dict)
    #Act

    Write.DataFrameToCSVFile(df)
    #Assert
    assert os.path.exists(fullPath)

def test_read_csv():
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = 'input.csv'
    path = 'tests/test_data'
    fullPath = path + '/' + filename
    #Act
    df = Read.DataFrameFromCSVFile()
    #Assert
    assert type(df) is pandas.DataFrame