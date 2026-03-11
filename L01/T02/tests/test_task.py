import unittest
from task import score, balance, quantity, total, value


class TestCase(unittest.TestCase):
    def test_score_value(self):
        self.assertEqual(score, 25, msg="score should equal 25. Add 10, then add 15 more.")

    def test_balance_value(self):
        self.assertEqual(balance, 65, msg="balance should equal 65. Subtract 25, then subtract 10 more.")

    def test_quantity_value(self):
        self.assertEqual(quantity, 30, msg="quantity should equal 30. Multiply by 3, then multiply by 2.")

    def test_total_value(self):
        self.assertEqual(total, 160, msg="total should equal 160. Add 30 first, then double the result.")

    def test_value_value(self):
        self.assertEqual(value, 30, msg="value should equal 30. Use floor division by 2, then subtract 20.")
