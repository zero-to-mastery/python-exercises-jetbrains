import unittest
from L06.T02 import task

class TestGame(unittest.TestCase):
    def test_input(self):
        result = task.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = task.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = task.run_guess(11, 5)
        self.assertFalse(result)

    # Note that we test run_guess directly, so add an isinstance(guess, int)
    # check and return False for string input.
    def test_input_wrong_type(self):
        result = task.run_guess('11', 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()