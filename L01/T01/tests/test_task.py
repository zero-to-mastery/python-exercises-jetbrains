import unittest
from task import result1, result2, result3, result4, result5


class TestCase(unittest.TestCase):
    def test_result1_value(self):
        self.assertEqual(result1, 45.0, msg="result1 should equal 45.0. Check the order of operations.")

    def test_result2_value(self):
        self.assertEqual(result2, 32, msg="result2 should equal 32. Remember: multiplication happens before addition.")

    def test_result3_value(self):
        self.assertEqual(result3, 12.0, msg="result3 should equal 12.0. Division happens before addition.")

    def test_result4_value(self):
        self.assertEqual(result4, 50, msg="result4 should equal 50. Use parentheses to control the order.")

    def test_result5_value(self):
        self.assertEqual(result5, 5, msg="result5 should equal 5. Floor division returns an integer result.")

    def test_result5_type(self):
        self.assertIsInstance(result5, int, msg="result5 should use floor division (//) to return an integer.")
