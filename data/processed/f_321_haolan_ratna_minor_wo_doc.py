import re
import urllib.request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def f_321(API_URL):
    """
    Get the public IP address of the current host from an API.
    
    Returns:
    str: The public IP address.
    
    Requirements:
    - re
    - urllib.request
    - json
    
    Example:
    >>> f_321(https://api.ipify.org?format=json)
    '192.168.1.1'
    """

    try:
        response = urllib.request.urlopen(API_URL)
        data = json.loads(response.read())
        ip = data['ip']
        if re.match(IP_REGEX, ip):
            return ip
        else:
            return 'Invalid IP address received'
    except Exception as e:
        return str(e)

import unittest
from unittest.mock import patch, Mock
import json
class TestCases(unittest.TestCase):
    API_URL = 'https://api.ipify.org?format=json'
    @patch('urllib.request.urlopen')
    def test_valid_ip(self, mock_urlopen):
        # Mocking a valid IP response
        mock_response = Mock()
        mock_response.read.return_value = json.dumps({'ip': '192.168.1.1'}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        
        result = f_321(self.API_URL)
        self.assertEqual(result, '192.168.1.1')
    @patch('urllib.request.urlopen')
    def test_invalid_ip(self, mock_urlopen):
        # Mocking an invalid IP response
        mock_response = Mock()
        mock_response.read.return_value = json.dumps({'ip': '500.500.500.500'}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        
        result = f_321(self.API_URL)
        self.assertEqual(result, '500.500.500.500')
    @patch('urllib.request.urlopen')
    def test_api_failure(self, mock_urlopen):
        # Mocking an API failure
        mock_urlopen.side_effect = Exception("API failure")
        
        result = f_321(self.API_URL)
        self.assertEqual(result, "API failure")
    @patch('urllib.request.urlopen')
    def test_missing_ip_key(self, mock_urlopen):
        # Mocking response missing the 'ip' key
        mock_response = Mock()
        mock_response.read.return_value = json.dumps({}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        
        result = f_321(self.API_URL)
        self.assertEqual(result, "'ip'")
    @patch('urllib.request.urlopen')
    def test_non_json_response(self, mock_urlopen):
        # Mocking a non-JSON response from API
        mock_response = Mock()
        mock_response.read.return_value = "Non-JSON response".encode('utf-8')
        mock_urlopen.return_value = mock_response