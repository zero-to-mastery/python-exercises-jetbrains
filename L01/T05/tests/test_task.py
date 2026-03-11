import unittest
from task import result1, result2, result3, result4, age


class TestCase(unittest.TestCase):
    def test_result1(self):
        self.assertEqual(result1, 200,
                        msg="result1 should be 200 (convert '150' to int and add 50)")

    def test_result2(self):
        self.assertEqual(result2, 47.0,
                        msg="result2 should be 47.0 (convert '23.5' to float and multiply by 2)")

    def test_result3(self):
        self.assertEqual(result3, "Total items: 42",
                        msg="result3 should be 'Total items: 42' (convert 42 to string and concatenate)")

    def test_result4(self):
        self.assertEqual(result4, "Rating: 4.8 stars",
                        msg="result4 should be 'Rating: 4.8 stars' (convert 4.8 to string and concatenate)")

    def test_age(self):
        self.assertEqual(age, 34,
                        msg="age should be 34 (2024 - 1990 after converting '1990' to int)")
