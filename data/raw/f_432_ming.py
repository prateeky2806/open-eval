import base64
import zlib
import random
import string

def f_432(string_length=100):
    """
    Create a random string of a specified length with uppercase letters and digits, compress it with zlib, 
    and then encode the compressed string in base64.

    Parameters:
    - string_length (int, optional): The length of the random string to be generated. Default is 100.

    Returns:
    str: The compressed string in base64.

    Requirements:
    - base64
    - zlib
    - random
    - string

    Example:
    >>> random.seed(1)
    >>> compressed_string = f_432(50)
    >>> print(compressed_string)
    eJxzNTH0CgqMMHJxMgkwdAyM8rQwc3IMMffzCHDyCAjy9PQI9HY0CY1wtzRx9YmKMg8wjgQAWN0NxA==
    """
    # Generate a random string
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))
    
    # Compress the string
    compressed_string = zlib.compress(random_string.encode('utf-8'))
    
    # Encode the compressed string in base64
    encoded_compressed_string = base64.b64encode(compressed_string)

    return encoded_compressed_string.decode('utf-8')

import unittest
import base64
import zlib

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_case_1(self):
        random.seed(1)
        result = f_432()
        self.assertEqual(result, 'eJxzNTH0CgqMMHJxMgkwdAyM8rQwc3IMMffzCHDyCAjy9PQI9HY0CY1wtzRx9YmKMg8wjgQAWN0NxA==')

    def test_case_2(self):
        random.seed(0)
        result = f_432(50)
        self.assertEqual(result, 'eJwzMQzwCvY38g4KMwv2Ngz3MrM0NvMxMIsMdAkIM7MIMvUyCnGM8jeOdAwy9fQxdQ/1tAAAVX8NdQ==')

    def test_case_3(self):
        random.seed(42)
        result = f_432(200)
        self.assertEqual(result, 'eJwFwVkCQCAQANArRZs+WzCTJIyU+x/Ee81GZF2F4uC20Agqt/zbl2kPQVTOyGTir3w+h5vHsL05Q9StrmzJpj1dDOhSBC1TO9QZ8YlVHWDu4MI7Fp8NTcJ+nWKbyznJeK9Kbq0uA41kk9WSJy+ncPlhmC+KsgAxSKaVe8a9IvgXlfDYYdbPNfI1lHKybsKxS1zPsqEukpwRP8dcNyU=')

    def test_case_4(self):
        random.seed(10)
        result = f_432(10)
        self.assertEqual(result, 'eJwLDQj1MDaOcAv2AQAQIQLm')

    def test_case_5(self):
        random.seed(1)
        result = f_432(1)
        self.assertEqual(result, 'eJxzBQAARgBG')
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()