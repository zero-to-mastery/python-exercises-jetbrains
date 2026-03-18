import importlib
import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch


def try_import():
    return importlib.import_module('task')


class TestCase(unittest.TestCase):
    task_name = 'task'

    def setUp(self):
        try:
            with patch('sys.stdout', new=StringIO()):
                if self.task_name in sys.modules:
                    del sys.modules[self.task_name]
                task_file = os.path.join(
                    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'task.py'
                )
                spec = importlib.util.spec_from_file_location(self.task_name, task_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules[self.task_name] = module
        except NameError:
            pass
        except Exception as e:
            self.fail(
                "There was a problem while loading the solution — {0}. "
                "Check the solution for IDE-highlighted errors and warnings."
                .format(str(e))
            )

    def test_basic_case(self):
        try:
            highest_even = try_import().highest_even
        except AttributeError:
            self.fail(msg="The function highest_even seems to be undefined.")

        result = highest_even([10, 2, 3, 4, 8, 11])
        self.assertEqual(
            result,
            10,
            msg="The function should return 10 for the list [10, 2, 3, 4, 8, 11]."
        )

    def test_empty_list(self):
        try:
            highest_even = try_import().highest_even
        except AttributeError:
            self.fail(msg="The function highest_even seems to be undefined.")

        with self.assertRaises(
            ValueError,
            msg="The function should raise ValueError for an empty list."
        ):
            highest_even([])

    def test_mixed_negative_and_duplicates(self):
        try:
            highest_even = try_import().highest_even
        except AttributeError:
            self.fail(msg="The function highest_even seems to be undefined.")

        result = highest_even([-5, 5, 1, -2, 3, -4, -4])
        self.assertEqual(
            result,
            -2,
            msg="The function should return -2 for the list [-5, 5, 5, 1, -2, 3, -4]."
        )


if __name__ == '__main__':
    unittest.main()