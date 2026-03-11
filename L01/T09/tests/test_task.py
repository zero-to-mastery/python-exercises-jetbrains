import unittest
from task import fruits, apple_count, numbers, count_twos


class TestCase(unittest.TestCase):
    def test_fruits_after_remove_banana(self):
        self.assertNotIn("Banana", fruits,
                        msg="'Banana' should be removed from fruits")

    def test_fruits_has_kiwi(self):
        self.assertIn("Kiwi", fruits,
                     msg="'Kiwi' should be added to fruits")

    def test_fruits_has_mango_at_start(self):
        self.assertEqual(fruits[0], "Mango",
                        msg="'Mango' should be at index 0 in fruits")

    def test_apple_count(self):
        self.assertEqual(apple_count, 1,
                        msg="apple_count should be 1 (count of 'Apples' in fruits)")

    def test_count_twos(self):
        self.assertEqual(count_twos, 3,
                        msg="count_twos should be 3 (count of 2 in numbers)")

    def test_numbers_after_remove(self):
        self.assertEqual(numbers.count(2), 2,
                        msg="After removing one 2, there should be 2 occurrences of 2 left in numbers")
