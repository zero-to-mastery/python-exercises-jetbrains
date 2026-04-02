import unittest
from L06.T01 import task

class TestDoStuff(unittest.TestCase):
    def test_with_five(self):
        result = task.do_stuff(5)
        self.assertEqual(result, 10)

    def test_with_string_number(self):
        result = task.do_stuff('7')
        self.assertEqual(result, 12)

    def test_with_invalid_string(self):
        result = task.do_stuff('hello')
        self.assertIsInstance(result, ValueError)

    # Add a special case for 0 in do_stuff() at `task.py` so that this test passes.
    def test_with_zero(self):
        result = task.do_stuff(0)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
