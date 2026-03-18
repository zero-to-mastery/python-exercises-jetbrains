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
        expected_value = ['SISI', 'BIBI', 'TITI', 'CARLA']

        try:
            actual_value = try_import().answer_1
        except AttributeError:
            self.fail(msg="The variable answer_1 seems to be undefined.")

        self.assertEqual(
            actual_value,
            expected_value,
            msg="answer_1 should contain all pet names in uppercase."
        )

    def test_answer_2(self):
        expected_value = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

        try:
            actual_value = try_import().answer_2
        except AttributeError:
            self.fail(msg="The variable answer_2 seems to be undefined.")

        self.assertEqual(
            actual_value,
            expected_value,
            msg="answer_2 should contain the strings zipped with the sorted numbers."
        )

    def test_answer_3(self):
        expected_value = [73, 65, 76, 100, 88]

        try:
            actual_value = try_import().answer_3
        except AttributeError:
            self.fail(msg="The variable answer_3 seems to be undefined.")

        self.assertEqual(
            actual_value,
            expected_value,
            msg="answer_3 should contain only scores above 50."
        )

    def test_answer_4(self):
        expected_value = 456

        try:
            actual_value = try_import().answer_4
        except AttributeError:
            self.fail(msg="The variable answer_4 seems to be undefined.")

        self.assertEqual(
            actual_value,
            expected_value,
            msg="answer_4 should contain the total of my_numbers and scores."
        )


if __name__ == '__main__':
    unittest.main()