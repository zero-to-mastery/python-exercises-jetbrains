import importlib.util
from io import StringIO
import os
import re
import sys
import unittest
from unittest.mock import patch


class TestCase(unittest.TestCase):
    task_name = 'formatted_strings_exercise'
    task_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'ExerciseFormattedStrings.py'
    )

    def setUp(self):
        self.import_error = None
        self.module = None
        try:
            with patch('sys.stdout', new=StringIO()):
                spec = importlib.util.spec_from_file_location(self.task_name, self.task_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules[self.task_name] = module
                self.module = module
        except SyntaxError as se:
            self.import_error = ("Syntax error while loading the solution – {0}. "
                                 "Please fill in all answers with valid numbers or strings "
                                 "(empty placeholders are invalid)."
                                 .format(str(se)))
        except Exception as e:
            self.import_error = ("There was a problem while loading the solution – {0}. Check the solution for "
                                 "IDE-highlighted errors and warnings.".format(str(e)))

    def test_answer_1(self):
        if self.import_error:
            self.fail(self.import_error)

        expected_value = 'Hello Cindy, your balance is 50.'

        try:
            actual_value = self.module.answer_1
        except AttributeError:
            self.fail(msg="The variable answer_1 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_1 value seems to be a bit off.")

    def test_answer_2(self):
        if self.import_error:
            self.fail(self.import_error)

        expected_value = 'Hello Cindy, your balance is 50.'

        try:
            actual_value = self.module.answer_2
        except AttributeError:
            self.fail(msg="The variable answer_2 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_2 value seems to be a bit off.")

    def test_answer_3(self):
        if self.import_error:
            self.fail(self.import_error)

        expected_value = 'Hello Cindy, your balance is 50.'

        try:
            actual_value = self.module.answer_3
        except AttributeError:
            self.fail(msg="The variable answer_3 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_3 value seems to be a bit off.")

    def test_ordered_4_f_string_version(self):
        if self.import_error:
            self.fail(self.import_error)

        expected_value = f"Hello {self.module.name}, your balance is {self.module.amount}."

        try:
            actual_value = self.module.f_string_version
        except AttributeError:
            self.fail(msg="The variable f_string_version seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The f_string_version value seems to be a bit off.")

        try:
            with open(self.task_file, 'r', encoding='utf-8') as handle:
                source = handle.read()
        except OSError:
            self.fail("Could not read the task file to verify the f-string syntax.")

        pattern = r'^[ \t]*f_string_version[ \t]*=[ \t]*f"Hello {name}, your balance is {amount}\."[ \t]*$'
        match = re.search(pattern, source, flags=re.MULTILINE)
        self.assertIsNotNone(
            match,
            msg="The f_string_version must be defined exactly as: "
                "f\"Hello {name}, your balance is {amount}.\""
        )


if __name__ == '__main__':
    unittest.main()
