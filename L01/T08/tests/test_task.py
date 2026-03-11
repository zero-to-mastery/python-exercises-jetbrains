import unittest
from task import oranges, apples, blueberries, five, nine


class TestCase(unittest.TestCase):
    def test_oranges(self):
        self.assertEqual(oranges, "Oranges",
                        msg="oranges should be 'Oranges' (accessed from basket[1][1][0])")

    def test_apples(self):
        self.assertEqual(apples, "Apples",
                        msg="apples should be 'Apples' (accessed from basket[1][0])")

    def test_blueberries(self):
        self.assertEqual(blueberries, "Blueberries",
                        msg="blueberries should be 'Blueberries' (accessed from basket[1][2])")

    def test_five(self):
        self.assertEqual(five, 5,
                        msg="five should be 5 (accessed from matrix[1][1])")

    def test_nine(self):
        self.assertEqual(nine, 9,
                        msg="nine should be 9 (accessed from matrix[2][2])")
