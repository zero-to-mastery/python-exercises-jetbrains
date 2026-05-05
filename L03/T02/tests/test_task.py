import importlib
import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch

TASK_NAME = 'for_loop_counter'
TASK_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'task.py'
)


def try_import():
    return importlib.import_module(TASK_NAME)


class TestCase(unittest.TestCase):
    task_name = TASK_NAME

    def setUp(self):
        try:
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                if self.task_name in sys.modules:
                    del sys.modules[self.task_name]
                spec = importlib.util.spec_from_file_location(TASK_NAME, TASK_FILE)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules[TASK_NAME] = module
        except NameError:
            pass
        except SyntaxError as se:
            self.fail("Syntax error while loading the solution — {0}. "
                      "Please fill in all answers with valid expressions (empty placeholders are invalid)."
                      .format(str(se)))
        except Exception as e:
            self.fail("There was a problem while loading the solution — {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_answer(self):
        expected_value = 55

        try:
            actual_value = try_import().counter
        except AttributeError:
            self.fail(msg="The variable answer seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The answer value seems to be a bit off.")


if __name__ == '__main__':
    unittest.main()
