import importlib
import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch
from types import GeneratorType


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

    def test_fib_exists(self):
        try:
            fib_function = try_import().fib
        except AttributeError:
            self.fail(msg="The function fib seems to be undefined.")

        self.assertTrue(
            callable(fib_function),
            msg="fib should be a function."
        )

    def test_fib_returns_generator(self):
        module = try_import()
        result = module.fib(5)

        self.assertIsInstance(
            result,
            GeneratorType,
            msg="fib(number) should return a generator."
        )

    def test_fib_5(self):
        expected_value = [0, 1, 1, 2, 3]
        actual_value = list(try_import().fib(5))

        self.assertEqual(
            actual_value,
            expected_value,
            msg="fib(5) should generate the first 5 Fibonacci numbers."
        )

    def test_fib_10(self):
        expected_value = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        actual_value = list(try_import().fib(10))

        self.assertEqual(
            actual_value,
            expected_value,
            msg="fib(10) should generate the first 10 Fibonacci numbers."
        )


if __name__ == '__main__':
    unittest.main()