import importlib
import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch

def try_import():
    return importlib.import_module('augmented_assignment')


class TestCase(unittest.TestCase):
    task_name = 'augmented_assignment'

    def setUp(self):
        try:
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                if self.task_name in sys.modules:
                    del sys.modules[self.task_name]
                task_file = os.path.join(
                    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'ExerciseAugmentedAssignmentOperator.py'
                )
                spec = importlib.util.spec_from_file_location(self.task_name, task_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules[self.task_name] = module
        except NameError:
            pass
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_prediction(self):
        expected_value = 6

        try:
            actual_value = try_import().prediction
        except AttributeError:
            self.fail(msg="The variable prediction seems to be undefined. Do not remove it from the task code.")

        self.assertEqual(expected_value, actual_value, msg="The prediction value seems to be a bit off.")


if __name__ == '__main__':
    unittest.main()
