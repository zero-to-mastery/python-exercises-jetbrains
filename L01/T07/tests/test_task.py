import unittest
from task import first_color, last_color, middle_colors, colors, combined_numbers, second_to_last


class TestCase(unittest.TestCase):
    def test_first_color(self):
        self.assertEqual(first_color, "red",
                        msg="first_color should be 'red' (first element of colors)")

    def test_last_color(self):
        self.assertEqual(last_color, "yellow",
                        msg="last_color should be 'yellow' (last element using negative index)")

    def test_middle_colors(self):
        self.assertEqual(middle_colors, ["green", "blue"],
                        msg="middle_colors should be ['green', 'blue'] (elements from index 1 to 2)")

    def test_colors_modification(self):
        self.assertEqual(colors[1], "purple",
                        msg="Second element of colors should be modified to 'purple'")

    def test_combined_numbers(self):
        self.assertEqual(combined_numbers, [1, 2, 3, 4, 5],
                        msg="combined_numbers should be [1, 2, 3, 4, 5] (concatenation of numbers1 and numbers2)")

    def test_second_to_last(self):
        self.assertEqual(second_to_last, "d",
                        msg="second_to_last should be 'd' (second to last element of letters)")
