import importlib
import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch


def try_import():
    return importlib.import_module('find_duplicates')


class TestCase(unittest.TestCase):
    task_name = 'find_duplicates'

    def setUp(self):
        try:
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
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

    def test_duplicates_found(self):
        expected_value = ['b', 'n']

        try:
            actual_value = try_import().duplicates
        except AttributeError:
            self.fail(msg="The variable 'answer' seems to be undefined.")

        self.assertEqual(
            sorted(expected_value),
            sorted(actual_value),
            msg="The duplicates list should contain 'b' and 'n'."
        )

if __name__ == '__main__':
    unittest.main()