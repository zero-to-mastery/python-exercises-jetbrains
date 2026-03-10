import importlib
import importlib.util
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch


def try_import():
    return importlib.import_module('type_conversion')


class TestCase(unittest.TestCase):
    task_name = 'type_conversion'

    def setUp(self):
        try:
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                if self.task_name in sys.modules:
                    importlib.reload(sys.modules[self.task_name])
                else:
                    task_file = os.path.join(
                        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        'ExerciseTypeConversion.py'
                    )
                    spec = importlib.util.spec_from_file_location(self.task_name, task_file)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    sys.modules[self.task_name] = module
        except NameError as ne:
            pass
        except Exception as e:
            self.fail("There was a problem while loading the solution – {0}. Check the solution for "
                      "IDE-highlighted errors and warnings.".format(str(e)))

    def test_age_type_and_value(self):
        try:
            age = try_import().age
        except AttributeError:
            self.fail(msg="The variable age seems to be undefined. "
                          "Do not remove it from the task code.")

        self.assertIsInstance(age, int, msg="The age variable has a wrong type. "
                                            "Make sure you convert birth_year using int().")
        self.assertGreater(age, 0, msg="The age variable should be greater than 0. "
                                       "Make sure you calculate it correctly.")


if __name__ == '__main__':
    unittest.main()
