import unittest
from task import template1, template2, template3, result1, result2, result3, result4, result5, result6, result7, result8


class TestCase(unittest.TestCase):
    def test_template1_format(self):
        """Test template1 can be used with .format()"""
        result = template1.format("phone", 599)
        self.assertEqual(result, "The phone costs $599.",
                        msg="template1 should work with .format() to produce formatted strings")

    def test_result1_and_result2(self):
        """Test that template1 produces correct results"""
        self.assertEqual(result1, "The laptop costs $999.",
                        msg="result1 should be 'The laptop costs $999.'")
        self.assertEqual(result2, "The keyboard costs $49.",
                        msg="result2 should be 'The keyboard costs $49.'")

    def test_template2_format(self):
        """Test template2 can be used with .format() and repeats first argument"""
        result = template2.format("Alice", 11111)
        self.assertEqual(result, "Alice placed order #11111. Thank you, Alice!",
                        msg="template2 should use {0} to repeat the customer name")

    def test_result3_and_result4(self):
        """Test that template2 produces correct results"""
        self.assertEqual(result3, "Sarah placed order #12345. Thank you, Sarah!",
                        msg="result3 should be 'Sarah placed order #12345. Thank you, Sarah!'")
        self.assertEqual(result4, "John placed order #67890. Thank you, John!",
                        msg="result4 should be 'John placed order #67890. Thank you, John!'")

    def test_template3_format(self):
        """Test template3 can be used with named placeholders"""
        result = template3.format(item="pen", qty=10, total=15)
        self.assertEqual(result, "Item: pen, Quantity: 10, Total: $15",
                        msg="template3 should use named placeholders {item}, {qty}, {total}")

    def test_result5_and_result6(self):
        """Test that template3 produces correct results"""
        self.assertEqual(result5, "Item: mouse, Quantity: 3, Total: $45",
                        msg="result5 should be 'Item: mouse, Quantity: 3, Total: $45'")
        self.assertEqual(result6, "Item: cable, Quantity: 5, Total: $25",
                        msg="result6 should be 'Item: cable, Quantity: 5, Total: $25'")

    def test_result7(self):
        """Test f-string with variables"""
        self.assertEqual(result7, "Alex scored 87 points.",
                        msg="result7 should be 'Alex scored 87 points.'")

    def test_result8(self):
        """Test f-string with expression"""
        self.assertEqual(result8, "Area: 50 square meters",
                        msg="result8 should calculate 10 * 5 = 50")
