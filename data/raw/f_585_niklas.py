import pandas as pd
import numpy as np

def f_585(data, cols):
    """
    Turn the provided data into a DataFrame and then calculate the correlation matrix of numeric columns.
    
    Parameters:
    - data (list): List of lists with the data, where the length of the inner list equals the number of columns
    - cols (list): List of column names
    
    Returns:
    - correlation_matrix (DataFrame): The correlation matrix.

    Requirements:
    - pandas
    - numpy
    
    Example:
    >>> correlation_matrix = f_585([[5.1, 3.5, 1.4], [4.9, 3.0, 1.4], [4.7, 3.2, 1.3]], ['x', 'y', 'z'])
    >>> print(correlation_matrix)
              x         y         z
    x  1.000000  0.596040  0.866025
    y  0.596040  1.000000  0.114708
    z  0.866025  0.114708  1.000000
    """
    df = pd.DataFrame(data, columns=cols)
    correlation_matrix = df.corr()
    return correlation_matrix ### Turn into numpy ###

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame([[5.1, 3.5, 1.4], [4.9, 3.0, 1.4], [4.7, 3.2, 1.3]], columns = ['x', 'y', 'z'])
        correlation_matrix = f_585([[5.1, 3.5, 1.4], [4.9, 3.0, 1.4], [4.7, 3.2, 1.3]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))

    def test_case_2(self):
        df = pd.DataFrame([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], columns = ['x', 'y', 'z'])
        correlation_matrix = f_585([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))

    def test_case_3(self):
        df = pd.DataFrame([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], columns = ['x', 'y', 'z'])
        correlation_matrix = f_585([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))
    
    def test_case_4(self):
        df = pd.DataFrame([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0]], columns = ['x', 'y', 'z'])
        correlation_matrix = f_585([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))

    def test_case_5(self):
        df = pd.DataFrame([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0], [-7.0, -8.0, -9.0]], columns = ['x', 'y', 'z'])
        correlation_matrix = f_585([[-1.0, -2.0, -3.0], [-4.0, -5.0, -6.0], [-7.0, -8.0, -9.0]], ['x', 'y', 'z'])
        self.assertTrue(np.allclose(correlation_matrix, df.corr()))

run_tests()
if __name__ == "__main__":
    run_tests()