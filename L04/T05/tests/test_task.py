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

    def test_answer_1(self):
        expected_value = [25, 16, 9]

        try:
            actual_value = try_import().answer_1
        except AttributeError:
            self.fail(msg="The variable answer_1 seems to be undefined.")

        self.assertEqual(
            actual_value,
            expected_value,
            msg="answer_1 should contain the squared values from my_list."
        )

    def test_answer_2(self):
        expected_value = [(10, -2), (0, 2), (4, 3), (9, 9)]

        try:
            actual_value = try_import().a
        except AttributeError:
            self.fail(msg="The variable `a` seems to be undefined.")

        self.assertEqual(
            actual_value,
            expected_value,
            msg="`a` should contain the tuples sorted by the second element."
        )


if __name__ == '__main__':
    unittest.main()