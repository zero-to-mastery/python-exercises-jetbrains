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

    def test_default_age(self):
        try:
            func = try_import().checkDriverAge
        except AttributeError:
            self.fail(msg="The function checkDriverAge seems to be undefined.")

        with patch('sys.stdout', new=StringIO()) as captured_output:
            func()
            output = captured_output.getvalue().strip()

        self.assertEqual(
            "Sorry, you are too young to drive this car. Powering off",
            output,
            msg="When called without arguments, the function should use the default age and print the correct message."
        )

    def test_age_16(self):
        try:
            func = try_import().checkDriverAge
        except AttributeError:
            self.fail(msg="The function checkDriverAge seems to be undefined.")

        with patch('sys.stdout', new=StringIO()) as captured_output:
            func(16)
            output = captured_output.getvalue().strip()

        self.assertEqual(
            "Sorry, you are too young to drive this car. Powering off",
            output,
            msg="For age 16, the function should print the correct message."
        )

    def test_age_18(self):
        try:
            func = try_import().checkDriverAge
        except AttributeError:
            self.fail(msg="The function checkDriverAge seems to be undefined.")

        with patch('sys.stdout', new=StringIO()) as captured_output:
            func(18)
            output = captured_output.getvalue().strip()

        self.assertEqual(
            "Congratulations on your first year of driving. Enjoy the ride!",
            output,
            msg="For age 18, the function should print the correct message."
        )

    def test_age_25(self):
        try:
            func = try_import().checkDriverAge
        except AttributeError:
            self.fail(msg="The function checkDriverAge seems to be undefined.")

        with patch('sys.stdout', new=StringIO()) as captured_output:
            func(25)
            output = captured_output.getvalue().strip()

        self.assertEqual(
            "Powering On. Enjoy the ride!",
            output,
            msg="For age 25, the function should print the correct message."
        )


if __name__ == '__main__':
    unittest.main()