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
    task_name = 'lists_exercise'
    task_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'Lists.py'
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
        expected_value = 'notebooks'

        try:
            actual_value = try_import(self.task_name).answer_1
        except AttributeError:
            self.fail(msg="The variable answer_1 seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer_1 value seems to be a bit off.")


if __name__ == '__main__':
    unittest.main()
