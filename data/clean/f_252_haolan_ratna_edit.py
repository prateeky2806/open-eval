import numpy as np
import pandas as pd
from random import uniform
from sklearn.preprocessing import StandardScaler

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def f_252(n_data_points=5000, min_value=0.0, max_value=10.0):
    """
    Generate a random dataset of floating point numbers, truncate each value to 3 decimal places and normalize the data using standard scaling (mean = 0, std = 1).
    
    Parameters:
    n_data_points (int): Number of data points to generate. Default is 5000.
    min_value (float): Minimum value range for data points. Default is 0.0.
    max_value (float): Maximum value range for data points. Default is 10.0.
    
    Returns:
    DataFrame: A pandas DataFrame with the normalized data.
    
    Note:
    - The function use "Normalized Value" for the column name in the DataFrame that being returned.

    Requirements:
    - numpy
    - pandas
    - random
    - sklearn.preprocessing

    Example:
    >>> normalized_data = f_252(5000, 5, 5)
    >>> print(normalized_data['Normalized Value'][0])
    0.0
    """
    if max_value < min_value:
        raise ValueError()

    data = [round(uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[['Value']])

    return pd.DataFrame(normalized_data, columns=['Normalized Value'])

import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        df = f_252()
        self.assertIsInstance(df, pd.DataFrame, "Return type should be a DataFrame.")
        self.assertEqual(len(df), 5000, "Default number of data points should be 5000.")
        self.assertAlmostEqual(df['Normalized Value'].mean(), 0, delta=0.1, msg="Mean should be close to 0.")
        self.assertAlmostEqual(df['Normalized Value'].std(), 1, delta=0.1, msg="Standard deviation should be close to 1.")

    def test_custom_parameters(self):
        df = f_252(1000, 1.0, 5.0)
        self.assertEqual(len(df), 1000, "Number of data points should match the specified value.")
        self.assertTrue(df['Normalized Value'].min() >= -3, "Normalized values should be within a reasonable range.")
        self.assertTrue(df['Normalized Value'].max() <= 3, "Normalized values should be within a reasonable range.")

    def test_edge_case_empty(self):
        with self.assertRaises(ValueError):
            f_252(0)

    def test_negative_data_points(self):
        with self.assertRaises(ValueError):
            f_252(-100)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            f_252(1000, 5.0, 1.0)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# Uncomment the below line to run the tests
# run_tests()
if __name__ == "__main__":
    run_tests()