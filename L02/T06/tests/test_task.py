import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch


class TestCase(unittest.TestCase):
    task_name = 'password_checker_exercise'
    task_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'ExercisePasswordChecker.py'
    )

    def setUp(self):
        self.import_error = None
        self.module = None
        try:
            with patch('sys.stdout', new=StringIO()), patch(
                'builtins.input',
                side_effect=['alice', 'SuperSecret123']
            ):
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

    def test_username_is_set(self):
        if self.import_error:
            self.fail(self.import_error)

        try:
            actual_value = self.module.username
        except AttributeError:
            self.fail(msg="The variable username seems to be undefined. Do not remove it from the task code.")

        self.assertIsInstance(actual_value, str, msg="The username should be a string.")
        self.assertTrue(actual_value, msg="The username should not be empty.")

    def test_password_is_set(self):
        if self.import_error:
            self.fail(self.import_error)

        try:
            actual_value = self.module.password
        except AttributeError:
            self.fail(msg="The variable password seems to be undefined. Do not remove it from the task code.")

        self.assertIsInstance(actual_value, str, msg="The password should be a string.")
        self.assertTrue(actual_value, msg="The password should not be empty.")

    def test_secret_password_is_masked(self):
        if self.import_error:
            self.fail(self.import_error)

        try:
            secret_password = self.module.secret_password
        except AttributeError:
            self.fail(msg="The variable secret_password seems to be undefined. Do not remove it from the task code.")

        self.assertIsInstance(secret_password, str, msg="The secret_password should be a string.")
        self.assertTrue(secret_password, msg="The secret_password should not be empty.")
        self.assertTrue(set(secret_password) == {'*'}, msg="The secret_password should contain only '*'.")
        self.assertEqual(
            '*' * len(self.module.password),
            secret_password,
            msg="The secret_password length should match the password length."
        )


if __name__ == '__main__':
    unittest.main()
