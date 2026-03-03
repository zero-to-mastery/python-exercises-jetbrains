import importlib
import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch

def try_import(task_name):
    return importlib.import_module(task_name)


class TestCase(unittest.TestCase):
    task_name = 'numbers_int_and_float'
    task_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'Int&Float.py'
    )

    def setUp(self):
        try:
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                if self.task_name in sys.modules:
                    del sys.modules[self.task_name]
                spec = importlib.util.spec_from_file_location(self.task_name, self.task_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules[self.task_name] = module
        except NameError:
            pass
        except SyntaxError as se:
            self.fail("Syntax error while loading the solution – {0}. "
                      "Please fill in all answers with valid numbers or strings (empty placeholders are invalid)."
                      .format(str(se)))
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_answer_1(self):
        expected_value = 6

        try:
            actual_value = try_import(self.task_name).answer_1
        except AttributeError:
            self.fail(msg="The variable answer_1 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_1 value seems to be a bit off.")

    def test_answer_2(self):
        expected_value = -2

        try:
            actual_value = try_import(self.task_name).answer_2
        except AttributeError:
            self.fail(msg="The variable answer_2 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_2 value seems to be a bit off.")

    def test_answer_3(self):
        expected_value = 8

        try:
            actual_value = try_import(self.task_name).answer_3
        except AttributeError:
            self.fail(msg="The variable answer_3 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_3 value seems to be a bit off.")

    def test_answer_4(self):
        expected_value = 0.5

        try:
            actual_value = try_import(self.task_name).answer_4
        except AttributeError:
            self.fail(msg="The variable answer_4 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_4 value seems to be a bit off.")

    def test_answer_5(self):
        expected_value = 'int'

        try:
            actual_value = try_import(self.task_name).answer_5
        except AttributeError:
            self.fail(msg="The variable answer_5 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_5 value seems to be a bit off.")

    def test_answer_6(self):
        expected_value = 'int'

        try:
            actual_value = try_import(self.task_name).answer_6
        except AttributeError:
            self.fail(msg="The variable answer_6 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_6 value seems to be a bit off.")

    def test_answer_7(self):
        expected_value = 'int'

        try:
            actual_value = try_import(self.task_name).answer_7
        except AttributeError:
            self.fail(msg="The variable answer_7 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_7 value seems to be a bit off.")

    def test_answer_8(self):
        expected_value = 'float'

        try:
            actual_value = try_import(self.task_name).answer_8
        except AttributeError:
            self.fail(msg="The variable answer_8 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_8 value seems to be a bit off.")

    def test_answer_9(self):
        expected_value = 'float'

        try:
            actual_value = try_import(self.task_name).answer_9
        except AttributeError:
            self.fail(msg="The variable answer_9 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_9 value seems to be a bit off.")

    def test_answer_10(self):
        expected_value = 11.0

        try:
            actual_value = try_import(self.task_name).answer_10
        except AttributeError:
            self.fail(msg="The variable answer_10 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_10 value seems to be a bit off.")

    def test_answer_11(self):
        expected_value = 8

        try:
            actual_value = try_import(self.task_name).answer_11
        except AttributeError:
            self.fail(msg="The variable answer_11 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_11 value seems to be a bit off.")

    def test_answer_12(self):
        expected_value = 1

        try:
            actual_value = try_import(self.task_name).answer_12
        except AttributeError:
            self.fail(msg="The variable answer_12 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_12 value seems to be a bit off.")

    def test_answer_13(self):
        expected_value = 2

        try:
            actual_value = try_import(self.task_name).answer_13
        except AttributeError:
            self.fail(msg="The variable answer_13 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_13 value seems to be a bit off.")

    def test_answer_14(self):
        expected_value = 3

        try:
            actual_value = try_import(self.task_name).answer_14
        except AttributeError:
            self.fail(msg="The variable answer_14 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_14 value seems to be a bit off.")

    def test_answer_15(self):
        expected_value = 4

        try:
            actual_value = try_import(self.task_name).answer_15
        except AttributeError:
            self.fail(msg="The variable answer_15 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_15 value seems to be a bit off.")

    def test_answer_16(self):
        expected_value = 20

        try:
            actual_value = try_import(self.task_name).answer_16
        except AttributeError:
            self.fail(msg="The variable answer_16 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_16 value seems to be a bit off.")

    def test_answer_17(self):
        expected_value = '0b101'

        try:
            actual_value = try_import(self.task_name).answer_17
        except AttributeError:
            self.fail(msg="The variable answer_17 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_17 value seems to be a bit off.")

    def test_answer_18(self):
        expected_value = 5

        try:
            actual_value = try_import(self.task_name).answer_18
        except AttributeError:
            self.fail(msg="The variable answer_18 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_18 value seems to be a bit off.")


if __name__ == '__main__':
    unittest.main()
