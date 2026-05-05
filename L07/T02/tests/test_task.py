import importlib
import sys
import unittest
from unittest.mock import Mock, patch


class TestCase(unittest.TestCase):
    task_name = 'task'

    def setUp(self):
        try:
            if self.task_name in sys.modules:
                self.module = importlib.reload(sys.modules[self.task_name])
            else:
                self.module = importlib.import_module(self.task_name)
        except NameError:
            pass
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_request_api_data_uses_requests_get(self):
        expected_url = 'https://api.pwnedpasswords.com/range/ABCDE'

        with patch.object(self.module.requests, 'get', return_value=Mock(status_code=200)) as mock_get:
            self.module.request_api_data('ABCDE')

        self.assertEqual(1, mock_get.call_count,
                         msg="The function should send one GET request to the API.")

        self.assertEqual((expected_url,), mock_get.call_args.args,
                         msg="The function should send a GET request to the API using "
                             "the first 5 characters of the hash.")

    def test_request_api_data_raises_runtime_error(self):
        with patch.object(self.module.requests, 'get', return_value=Mock(status_code=500)):
            with self.assertRaises(RuntimeError,
                                   msg="The function should raise RuntimeError if the API response "
                                       "status code is not 200."):
                self.module.request_api_data('ABCDE')

    def test_get_password_leaks_count_returns_matching_count(self):
        mock_response = Mock()
        mock_response.text = "ABCDEF123:7\nZZZZZZ999:3"

        result = self.module.get_password_leaks_count(mock_response, "ABCDEF123")

        self.assertEqual("7", result,
                         msg="The function should split the response text into suffix-count pairs "
                             "and return the count for the matching suffix.")

    def test_pwned_api_check_uses_uppercase_sha1_prefix(self):
        mock_response = Mock()
        mock_response.text = ""

        with patch.object(self.module, 'request_api_data', return_value=mock_response) as mock_request:
            with patch.object(self.module, 'get_password_leaks_count', return_value=0):
                self.module.pwned_api_check('password')

        self.assertEqual(1, mock_request.call_count,
                         msg="The function should call request_api_data() once.")

        self.assertEqual(('5BAA6',), mock_request.call_args.args,
                         msg="The function should build an uppercase SHA-1 hash "
                             "and send its first 5 characters to the API.")